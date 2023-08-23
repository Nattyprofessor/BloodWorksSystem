import datetime
import json
import random
import time
import uuid

from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views.generic import TemplateView

from donor.functions import notify_admin_about_new_donor
from .models import *
from blood import models as b_models
from donor import functions as d_functions
from appointments import models as a_models, functions
from donor import models as d_models, forms as d_forms
from .function import *
from .forms import *

# ####Constants for pdf template Ids
DONATION_TEMPLATE = 'donation_template.html'
DONOR_TEMPLATE = 'donors_template.html'
EXAM_TEMPLATE = 'exam_template.html'
COLLECTED_DONATION_TEMPLATE = "donor_approval_template.html"

# Create your views here.
@login_required(login_url='volunteerlogin')
def volunteer_dashboard_view(request):
    volunteer = a_models.VolunteerRegistration.objects.get(user=request.user.id)

    donation_reports = DonationReport.objects.filter(volunteer=volunteer.volunteer_id).count()
    donor_reports = DonorReport.objects.filter(volunteer=volunteer.volunteer_id).count()

    pre_exam_counts = d_models.PreExamInfo.objects.filter(volunteer_id=volunteer.volunteer_id).count()
    pending_exams = d_models.PreExamInfo.objects.all().filter(volunteer_id=volunteer.volunteer_id).filter(
        status='Pending').count(),

    donors_served_count = d_models.Donor.objects.filter(served_by=volunteer.volunteer_id).count()
    print(volunteer.volunteer_id)
    return render(request, 'volunteer/volunteer_dashboard.html',
                  {'volunteer': volunteer, 'exams_count': pre_exam_counts, 'donors_served_count': donors_served_count,
                   'reports_count': donation_reports + donor_reports, 'pending_exams': len(pending_exams)})


def search_donor(request):
    # Check if the request is a post request.
    healthform = d_forms.DonorHealthForm()
    search_form = d_forms.SearchDonor()

    if request.method == 'POST':
        print('<>')
        if 'searchbtn' in request.POST:
            search_query = request.POST.get('search_donor', "Search")
            # search_query = search_form.data('search_donor')
            print(search_query, "<><>")
            try:
                donor = d_models.Donor.objects.get(donor_id=search_query)
            except:
                messages.success(request, 'No donor was found')

            else:
                messages.success(request, f'Donor with {donor.donor_id} has been found')
                return render(request, 'volunteer/update_donor.html',
                              {'searchform': search_form, 'donor': donor, 'healthform': healthform})

        if 'healthbtn' in request.POST:
            healthform = d_forms.DonorHealthForm(request.POST)

            print(healthform.errors)

            # healthform.data['taken_on'] = datetime.datetime
            x = healthform.save(commit=False)
            x.taken_on = datetime.datetime.now()

            if healthform.is_valid():

                healthform.save()

                messages.success(request, "Donor's Health Info has been saved")
                return render(request, 'volunteer/update_donor.html',
                              {'searchform': search_form, 'donor': x.donor_id, 'healthform': healthform})
            else:
                messages.error(request, "Donor's Health Info was not saved")
                messages.error(request, healthform.errors)

    return render(request, 'volunteer/update_donor.html', {'healthform': healthform, 'searchform': search_form})


def pre_exam_view(request):
    the_volunteer = a_models.VolunteerRegistration.objects.get(user=request.user)
    # Check if the request is a post request.
    exam_form = d_forms.PreExamForm()
    search_form = d_forms.SearchDonor()

    if request.method == 'POST':
        exam_form = d_forms.PreExamForm(request.POST)
        if exam_form.is_valid():
            form = exam_form.save(commit=False)
            form.pre_exam_id = generate_exam_id()

            form.save()

            donor = d_models.Donor.objects.get(donor_id=exam_form.data['donor_id'])

            current_date = datetime.datetime.now().strftime("%d/%m/%Y")
            payload = {
                "volunteer_id": f"{the_volunteer.volunteer_id}",
                "name": f"{donor.get_name}",
                "donor_id": f"{donor.donor_id}",
                "age": f"N/A",
                "blood_group": f"{donor.bloodgroup}",
                "station_name": f"{the_volunteer.blood_drive.name}",
                "donation_date": f"{current_date}",

                "exam": {
                    "volunteer_name": f"{the_volunteer.name}",
                    "id": f"{form.pre_exam_id}",
                    "haemoglobin_gDL": f"{exam_form.cleaned_data['haemoglobin_gDL']}",
                    "temperature_C": f"{exam_form.cleaned_data['temperature_C']}",
                    "blood_pressure": f"{exam_form.cleaned_data['blood_pressure']}",
                    "pulse_rate_BPM": f"{exam_form.cleaned_data['pulse_rate_BPM']}",
                }
            }
            exam =  {
                    "volunteer_name": f"{the_volunteer.name}",
                    "id": f"{form.pre_exam_id}",
                    "haemoglobin_gDL": f"{exam_form.cleaned_data['haemoglobin_gDL']}",
                    "temperature_C": f"{exam_form.cleaned_data['temperature_C']}",
                    "blood_pressure": f"{exam_form.cleaned_data['blood_pressure']}",
                    "pulse_rate_BPM": f"{exam_form.cleaned_data['pulse_rate_BPM']}",
                }
            report_data = generate_exam_report('exam', EXAM_TEMPLATE, payload, exam)
            #report_data = generate_my_report('exam', EXAM_TEMPLATE, payload)

            if report_data['status'] == 'success':

                url = report_data['doc_path']

                if url != 'error':
                    return HttpResponseRedirect(f"/{url}")

                else:
                    messages.error(request, "Some errors occured while generating the report")
                    messages.error(request, report_data)
                    return render(request, 'volunteer/donor_exam.html',
                                  {'examform': exam_form, 'searchform': search_form})
            messages.success(request, "The exam form has been saved to the donor's details")
            return render(request, 'volunteer/donor_exam.html', {'examform': exam_form})
        else:
            messages.error(request, "Some errors have occured while saving the form")
            messages.error(request, exam_form.errors)
            return render(request, 'volunteer/donor_exam.html', {'examform': exam_form})

    return render(request, 'volunteer/donor_exam.html', {'examform': exam_form, 'searchform': search_form})


def register_donor(request):
    userForm = d_forms.DonorUserForm()
    donorForm = d_forms.DonorForm()
    mydict = {'userForm': userForm, 'donorForm': donorForm}
    if request.method == 'POST':
        print('<>')
        userForm = d_forms.DonorUserForm(request.POST)
        donorForm = d_forms.DonorForm(request.POST, request.FILES)
        if userForm.is_valid() and donorForm.is_valid():
            print('<>')
            user = userForm.save(commit=False)
            if user.username == 'user':
                user.username = f"{user.last_name}{random.randrange(0, 200)}"

            user.set_password(str(uuid.uuid4()))
            user.save()
            donor = donorForm.save(commit=False)
            donor.user = user
            donor.bloodgroup = donorForm.cleaned_data['bloodgroup']
            donor.save()
            my_donor_group = Group.objects.get_or_create(name='DONOR')
            my_donor_group[0].user_set.add(user)

            user_name = user.first_name + " " + user.last_name
            #notify_admin_about_new_donor(donor, user_name)  # remove when uploading to server
            response = d_functions.generate_id_document(user_name, donor)
            if response == "success":
                messages.success(request, "Donor ID Card has been generated and saved.")
            else:
                messages.error(request, "There was an error in generating the donor's card id")
                messages.error(request, "Please login as the root admin and perform the task manually")
            return HttpResponseRedirect('/volunteer/update-donor')
        else:
            messages.error(request, 'There was an error in registering the donor')
            messages.error(request, donorForm.errors)
            messages.error(request, userForm.errors)
            return render(request, 'volunteer/register_donor.html', context=mydict)

    return render(request, 'volunteer/register_donor.html', context=mydict)


def donate_blood_view(request):
    the_volunteer = a_models.VolunteerRegistration.objects.get(user=request.user)

    station_id = the_volunteer.blood_drive.drive_id
    donationform = d_forms.DonationForm()
    if request.method == 'POST':
        donationform = d_forms.DonationForm(request.POST)
        if donationform.is_valid():
            blood_donate = donationform.save(commit=False)

            current_date = datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S")
            blood_donate.current_date = current_date
            blood_donate.donation_id = f"{station_id}-D-{random.randrange(0, 100)}-{str(current_date)}"
            blood_donate.save()

            print('XXXXX',blood_donate.donation_type)

            stock_count = b_models.Stock.objects.get(bloodgroup=blood_donate.blood_group)
            stock_count.unit += 1
            stock_count.save()

            #Generate a donation document for the user
            payload = {
                  "name": blood_donate.donor.get_name,
                  "age": blood_donate.age,
                  "blood_group": blood_donate.blood_group,
                  "units": blood_donate.unit,
                  "type": str(blood_donate.donation_type),
                  "donation_date": current_date,
                  "station_name": the_volunteer.blood_drive.name
            }
            response = generate_donor_statement(blood_donate.donor.donor_id,COLLECTED_DONATION_TEMPLATE,payload)
            if response['status'] == 'success':

                donor_notification = d_models.Notifications(donor=blood_donate.donor,
                                                            sender=request.user,
                                                            title="Blood Donation",
                                                            message="Thank you for donating your blood",
                                                            attachment=response['doc_path'],
                                                            created_date=timezone.datetime.now())
                donor_notification.save()
            messages.success(request, "New donation record saved to database")
            return HttpResponseRedirect('/volunteer/volunteer-dashboard/')
        else:
            messages.error(request, "error when adding the donation record")
            messages.error(request, donationform.errors)
            return render(request, 'volunteer/donate_blood.html', {'donationform': donationform})

    return render(request, 'volunteer/donate_blood.html', {'donationform': donationform})


def donation_reports_view(request):
    the_volunteer = a_models.VolunteerRegistration.objects.get(user=request.user)
    reports = DonationReport.objects.filter(volunteer=the_volunteer.volunteer_id)
    return render(request, 'volunteer/donation_reports.html', {'reports': reports})


# this view is dedicated to generate individual volunteer donation reports
def generate_donation_report(request):
    the_volunteer = a_models.VolunteerRegistration.objects.get(user=request.user)

    reports_count = DonationReport.objects.all().count()

    all_donations = d_models.BloodDonate.objects.all()
    # donation_array = list(all_donations)
    donation_array = [d.json(volunteer_id=the_volunteer.volunteer_id) for d in all_donations]

    print(donation_array, the_volunteer.blood_drive)
    # print(donation_array[0].donor.user.first_name)
    current_date = datetime.datetime.now().strftime("%d/%m/%Y")

    payload = {
        "station_name": f"{the_volunteer.blood_drive.name}",
        "station_id": f"{the_volunteer.blood_drive.drive_id}",
        "volunteer_id": f"{the_volunteer.volunteer_id}",
        "document_number": f"000{reports_count}",
        "document_date": f"{current_date}",

        "donors": donation_array
    }
    report_data = generate_donations_report('donation', DONATION_TEMPLATE, payload)
    #
    if report_data != 'error':
        generated_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #doc_path = generate_doc_path(report_data['document']['id'], report_data['document']['meta'], 'donation-reports')

        # save the new report to the database
        new_report = DonationReport(the_volunteer.volunteer_id, report_data['id'],
                                    the_volunteer.blood_drive.drive_id,
                                    "Donation_report", report_data['doc_path'], generated_date)
        new_report.save()
        messages.success(request, "Donation report generated successfully and saved to files")
        return HttpResponseRedirect('/volunteer/donation-reports')
    else:
        messages.error(request, "There was an error generating a new report")
        print('An error occurred')
        return HttpResponseRedirect('/volunteer/donation-reports')

    return HttpResponseRedirect(('/volunteer/donation-reports'))


def donor_reports_view(request):
    the_volunteer = a_models.VolunteerRegistration.objects.get(user=request.user)
    reports = DonorReport.objects.filter(volunteer=the_volunteer.volunteer_id)
    return render(request, 'volunteer/donors_reports.html', {'reports': reports})


def generate_donor_report(request):
    the_volunteer = a_models.VolunteerRegistration.objects.get(user=request.user)

    reports_count = DonorReport.objects.all().count()

    all_donors = d_models.Donor.objects.all()
    # donation_array = list(all_donations)
    donors_array = [d.json() for d in all_donors]

    print(donors_array, the_volunteer.blood_drive)
    # print(donation_array[0].donor.user.first_name)
    current_date = datetime.datetime.now().strftime("%d/%m/%Y")
    payload = {
        "station_name": f"{the_volunteer.blood_drive.name}",
        "station_id": f"{the_volunteer.blood_drive.drive_id}",
        "volunteer_id": f"{the_volunteer.volunteer_id}",
        "document_number": f"000{reports_count}",
        "document_date": f"{current_date}",

        "donors": donors_array
    }
    report_data = generate_donors_report('donor', DONOR_TEMPLATE, payload)
    #
    if report_data['status'] == 'success':
        generated_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # save the new report to the database
        new_report = DonorReport(the_volunteer.volunteer_id, report_data['id'],
                                 the_volunteer.blood_drive.drive_id,
                                 "Donor-report", report_data['doc_path'], generated_date)
        new_report.save()
        messages.success(request, "Donor report generated successfully and saved to files")
        return HttpResponseRedirect('/volunteer/donor-reports')
    else:
        messages.error(request, "There was an error generating a new report")
        print('An error occurred')
        return HttpResponseRedirect('/volunteer/donor-reports')

    return HttpResponseRedirect(('/volunteer/donation-reports'))


@user_passes_test(lambda user: user.is_staff)
def generate_station_report(request):
    the_volunteer = a_models.VolunteerRegistration.objects.get(user=request.user)
    current_date = datetime.datetime.now().strftime("%Y/%m/%d")

    station_name = the_volunteer.blood_drive.name
    station_id = the_volunteer.blood_drive.drive_id

    def get_progress(num_1, num_2):
        if num_1 == 0 and num_2 == 0:
            return 0
        else:
            x = (num_1 + num_2) * 100
            return int(x / (num_1 + num_2))

    donors = {"count": d_models.Donor.objects.filter(status="Approved").count(),
              "difference": d_models.Donor.objects.filter(status="Rejected").count()}

    # donors.progress = get_progress(donors.count, donors.difference)
    donors["progress"] = get_progress(donors['count'], donors['difference'])
    print(donors)

    units = {
        "count": d_models.BloodDonate.objects.filter(status="Approved").count(),
        "difference": d_models.BloodDonate.objects.filter(status="Rejected").count(),
    }
    units["progress"] = get_progress(units['count'], units['difference'])
    print(units)

    exams = {
        "count": d_models.PreExamInfo.objects.filter(status="Approved").count(),
        "difference": d_models.PreExamInfo.objects.filter(status="Rejected").count(),
    }

    exams["progress"] = get_progress(exams['count'], exams['difference'])
    print(exams)

    count = [d_models.BloodDonate.objects.filter(donation_type="1").count(),
             d_models.BloodDonate.objects.filter(donation_type="2").count(),
             d_models.BloodDonate.objects.filter(donation_type="3").count(),
             d_models.BloodDonate.objects.filter(donation_type="4").count()]

    colors = ["#00C3C1", "#FF5382", "#00A2F3", "#FF9B18"]

    def count_occurrences_after_two_hours(activities):

        final_list = [0, 0, 0, 0, 0]
        list01 = ["06", "07", "08"]
        list02 = ["09", "10", "11"]
        list03 = ["12", "13", "14"]
        list04 = ["15", "16", "17"]
        list05 = ["18", "19"]

        for activity in activities:
            print(activity.created_date)
            time_string = str(activity.created_date)
            # Stripping the offset from the date
            current_time = datetime.datetime.strptime(time_string[:19], '%Y-%m-%d %H:%M:%S')

            hour = str(current_time.time())[0:2]

            if hour in list01:
                final_list[0] += 1
            elif hour in list02:
                final_list[1] += 1
            elif hour in list03:
                final_list[2] += 1
            elif hour in list04:
                final_list[3] += 1
            elif hour in list05:
                final_list[4] += 1

        return final_list

    payload = {
        "current_date": current_date,
        "station_name": station_name,
        "station_id": station_id,
        "colors": colors,
        "donors": donors,
        "units": units,
        "exams": exams,
        "station_activity": {
            "time": ["6-8", "9-10", "11-13", "14-16", "17-19"],
            "values": [
                {"name": "New registrations", "data": count_occurrences_after_two_hours(d_models.Donor.objects.all())},
                {"name": "Blood collection",
                 "data": count_occurrences_after_two_hours(d_models.BloodDonate.objects.all())},
                {"name": "Pre exams done",
                 "data": count_occurrences_after_two_hours(d_models.PreExamInfo.objects.all())},
            ]
        },
        "donation_type": {
            "type": ["Blood", "Plasma", "Power Red", "Platelets"],
            "count": count
        }

    }
    print(payload)

    if not check_station_time():
        response = create_station_report(payload=payload)
        print(response)
        if response != 'error':
            report_id = response['document']['id']
            time.sleep(3)
            doc_path = generate_doc_path(report_id, response['document']['meta'], 'station-reports')
            print(f"The doc path for later use: {doc_path}")

            generated_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            new_report = StationReport(the_volunteer.volunteer_id, report_id, station_id, f"StationReport-{station_id}",
                                       doc_path, generated_date)
            new_report.save()

            report_url = get_document_url(report_id)
            return HttpResponseRedirect(report_url)
        else:
            print("Error in generating report")
            messages.error(request, "Error in generating report")
            return HttpResponseRedirect('/volunteer/volunteer-dashboard')
    else:
        print('Creating station report is not available at this time')
        messages.error(request, 'Creating station report is not available at this time')
        return HttpResponseRedirect('/volunteer/volunteer-dashboard')


def download_donor_report(request, pk):
    #report_url = get_document_url(pk)
    report = DonorReport.objects.get(report_id=pk)

    return HttpResponseRedirect(report.file.url)
def download_donation_report(request, pk):
    #report_url = get_document_url(pk)
    report = DonationReport.objects.get(report_id=pk)

    return HttpResponseRedirect(report.file.url)
def download_exam_report(request, pk):
    #report_url = get_document_url(pk)
    report = PreExamsReport.objects.get(report_id=pk)

    return HttpResponseRedirect(report.file.url)

class UploadReportView(TemplateView):
    template_name = 'volunteer/upload_reports.html'


def upload_report(request):
    print(request.FILES)
    messages.success(request, "Report uploaded successfully")
    return HttpResponseRedirect('/volunteer/volunteer-dashboard')
