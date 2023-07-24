import datetime
import time

from django.shortcuts import render, redirect, reverse
from . import forms, models
from django.db.models import Sum, Q, Count
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.conf import settings
from datetime import date, timedelta
from django.core.mail import send_mail
from django.contrib.auth.models import User
from donor import models as dmodels, functions
from patient import models as pmodels
from donor import forms as dforms, functions as dfunctions
from patient import forms as pforms
from appointments import models as amodels
from appointments import forms as aforms
from volunteer import function as vfunctions, models as vmodels
from .functions import *

def home_view(request):
    x = models.Stock.objects.all()
    print(x)

    hospitals = models.BloodDrives.objects.all().filter(name__contains='Hospital').count()
    donors = dmodels.Donor.objects.all().count()
    blood = dmodels.BloodDonate.objects.all().count()
    volunteers = amodels.VolunteerRegistration.objects.all().count()

    info = {
        'hospitals': hospitals,
        'donors': donors,
        'blood': blood,
        'volunteers': volunteers
    }
    if len(x) == 0:
        blood1 = models.Stock()
        blood1.bloodgroup = "A+"
        blood1.save()

        blood2 = models.Stock()
        blood2.bloodgroup = "A-"
        blood2.save()

        blood3 = models.Stock()
        blood3.bloodgroup = "B+"
        blood3.save()

        blood4 = models.Stock()
        blood4.bloodgroup = "B-"
        blood4.save()

        blood5 = models.Stock()
        blood5.bloodgroup = "AB+"
        blood5.save()

        blood6 = models.Stock()
        blood6.bloodgroup = "AB-"
        blood6.save()

        blood7 = models.Stock()
        blood7.bloodgroup = "O+"
        blood7.save()

        blood8 = models.Stock()
        blood8.bloodgroup = "O-"
        blood8.save()

    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'blood/index.html', context={'info':info})


def is_donor(user):
    return user.groups.filter(name='DONOR').exists()


def is_volunteer(user):
    return user.groups.filter(name="VOLUNTEER").exists()


def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()


def afterlogin_view(request):
    if is_donor(request.user):
        print('is_User')
        return redirect('donor/donor-dashboard')
    elif is_volunteer(request.user):
        print('is_Volunteer')
        return redirect('volunteer/volunteer-dashboard')
    elif is_patient(request.user):
        print('is_Patient')
        return redirect('patient/patient-dashboard')
    else:
        return redirect('admin-dashboard')

@user_passes_test(lambda user: user.is_superuser)
@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    totalunit = models.Stock.objects.aggregate(Sum('unit'))
    dict = {

        'A1': models.Stock.objects.get(bloodgroup="A+"),
        'A2': models.Stock.objects.get(bloodgroup="A-"),
        'B1': models.Stock.objects.get(bloodgroup="B+"),
        'B2': models.Stock.objects.get(bloodgroup="B-"),
        'AB1': models.Stock.objects.get(bloodgroup="AB+"),
        'AB2': models.Stock.objects.get(bloodgroup="AB-"),
        'O1': models.Stock.objects.get(bloodgroup="O+"),
        'O2': models.Stock.objects.get(bloodgroup="O-"),
        'totaldonors': dmodels.Donor.objects.all().filter(status='Approved').count(),
        'totalbloodunit': totalunit['unit__sum'],
        'totalrequest': models.BloodRequest.objects.all().count(),
        'totalapprovedrequest': models.BloodRequest.objects.all().filter(status='Approved').count()
    }
    return render(request, 'blood/admin_dashboard.html', context=dict)


@login_required(login_url='adminlogin')
def admin_blood_view(request):
    dict = {
        'bloodForm': forms.BloodForm(),
        'A1': models.Stock.objects.get(bloodgroup="A+"),
        'A2': models.Stock.objects.get(bloodgroup="A-"),
        'B1': models.Stock.objects.get(bloodgroup="B+"),
        'B2': models.Stock.objects.get(bloodgroup="B-"),
        'AB1': models.Stock.objects.get(bloodgroup="AB+"),
        'AB2': models.Stock.objects.get(bloodgroup="AB-"),
        'O1': models.Stock.objects.get(bloodgroup="O+"),
        'O2': models.Stock.objects.get(bloodgroup="O-"),
    }
    if request.method == 'POST':
        bloodForm = forms.BloodForm(request.POST)
        if bloodForm.is_valid():
            bloodgroup = bloodForm.cleaned_data['bloodgroup']
            stock = models.Stock.objects.get(bloodgroup=bloodgroup)
            stock.unit = bloodForm.cleaned_data['unit']
            stock.save()
        return HttpResponseRedirect('admin-blood')
    return render(request, 'blood/admin_blood.html', context=dict)


@login_required(login_url='adminlogin')
def admin_donor_view(request):
    approved_donors = dmodels.Donor.objects.all().filter(status='Approved')
    pending_donors = dmodels.Donor.objects.all().filter(status='Pending')
    rejected_donors = dmodels.Donor.objects.all().filter(status='Rejected')
    content = {
        'approved_donors': approved_donors,
        'pending_donors': pending_donors,
        'rejected_donors': rejected_donors
    }
    return render(request, 'blood/admin_donor.html', context=content)


@login_required(login_url='adminlogin')
def update_donor_view(request, id):
    donor = dmodels.Donor.objects.get(donor_id=id)
    user = dmodels.User.objects.get(id=donor.user_id)

    userForm = dforms.DonorUserForm(instance=user)
    donorForm = dforms.DonorForm(request.FILES, instance=donor)
    mydict = {'userForm': userForm, 'donorForm': donorForm, 'user': user, 'donor': donor}

    if request.method == 'POST':
        userForm = dforms.DonorUserForm(request.POST, instance=user)
        donorForm = dforms.DonorForm(request.POST, request.FILES, instance=donor)

        donor.status = donorForm.data['status']
        donor.bloodgroup = donorForm.data['bloodgroup']

        donor.save(update_fields=['status', 'bloodgroup'])
        messages.success(request, "Donor status has been updated")

        if donor.status == "Approved":
            if str(type(
                    donor.donor_card_code)) == "<class 'NoneType'>":  # means that the no card has ever been generated for the donor
                code = f'{donor.address} - {donor.user_id}'
                card_id = functions.generate_id_document(donor.get_name, donor, code)
                if card_id != "error":
                    donor.donor_card_code = card_id
                    donor.save(update_fields=['donor_card_code'])
                    messages.success(request, "Donor ID Card has been generated and saved.")
                else:
                    messages.error(request, "There was an error in generating the donor's card id")
                    messages.error(request, "Please login as the root admin and perform the task manually")
            else:
                print("the donor already has a donor card")

    return render(request, 'blood/update_donor.html', context=mydict)


@login_required(login_url='adminlogin')
def delete_donor_view(request, pk):
    donor = dmodels.Donor.objects.get(donor_id=pk)
    user = User.objects.get(id=donor.user_id)
    user.delete()
    donor.delete()
    return HttpResponseRedirect('/admin-donor')


@user_passes_test(lambda user: user.is_superuser)
@login_required(login_url='adminlogin')
def assign_volunteer_view(request, id):
    volunteer = amodels.VolunteerRegistration.objects.get(volunteer_id=id)
    print(volunteer)

    volunteer_form = aforms.VolunteerRegistrationForm(instance=volunteer, location=volunteer.location)
    mydict = {'volunteerForm': volunteer_form, 'volunteer': volunteer, }

    if request.method == 'POST':
        volunteer_form = aforms.VolunteerRegistrationForm(request.POST, instance=volunteer)

        drive = models.BloodDrives.objects.get(drive_id=volunteer_form.data['blood_drive'])

        volunteer.blood_drive = drive

        volunteer.save(update_fields=['blood_drive'])
        messages.success(request, "Volunteer has been assigned")

        dfunctions.notify_volunteer_of_assignment(volunteer)

        # Create an account for the volunteer
        volunteer.user = vfunctions.create_volunteer_account(volunteer)
        volunteer.save(update_fields=['user'])
        messages.success(request, "Volunteer account has been generated")

    return render(request, 'blood/assign_volunteer.html', context=mydict)


@login_required(login_url='adminlogin')
def reject_volunteer_view(request, id):
    volunteer = amodels.VolunteerRegistration.objects.get(volunteer_id=id)

    volunteer.delete()
    return HttpResponseRedirect('/admin-volunteers')


@login_required(login_url='adminlogin')
def admin_patient_view(request):
    patients = pmodels.Patient.objects.all()
    return render(request, 'blood/admin_patient.html', {'patients': patients})


@login_required(login_url='adminlogin')
def update_patient_view(request, pk):
    patient = pmodels.Patient.objects.get(id=pk)
    user = pmodels.User.objects.get(id=patient.user_id)
    userForm = pforms.PatientUserForm(instance=user)
    patientForm = pforms.PatientForm(request.FILES, instance=patient)
    mydict = {'userForm': userForm, 'patientForm': patientForm}
    if request.method == 'POST':
        userForm = pforms.PatientUserForm(request.POST, instance=user)
        patientForm = pforms.PatientForm(request.POST, request.FILES, instance=patient)
        if userForm.is_valid() and patientForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            patient = patientForm.save(commit=False)
            patient.user = user
            patient.bloodgroup = patientForm.cleaned_data['bloodgroup']
            patient.save()
            return redirect('admin-patient')
    return render(request, 'blood/update_patient.html', context=mydict)


@login_required(login_url='adminlogin')
def delete_patient_view(request, pk):
    patient = pmodels.Patient.objects.get(id=pk)
    user = User.objects.get(id=patient.user_id)
    user.delete()
    patient.delete()
    return HttpResponseRedirect('/admin-patient')


@login_required(login_url='adminlogin')
def admin_request_view(request):
    requests = models.BloodRequest.objects.all().filter(status='Pending')
    return render(request, 'blood/admin_request.html', {'requests': requests})


@login_required(login_url='adminlogin')
def admin_request_history_view(request):
    requests = models.BloodRequest.objects.all().exclude(status='Pending')
    return render(request, 'blood/admin_request_history.html', {'requests': requests})


@login_required(login_url='adminlogin')
def admin_show_appointments_view(request):
    print(request.POST)
    context = {'data': amodels.Appointment.objects.all(), 'form': aforms.AppointmentForm()}
    return render(request, 'blood/admin-appointment.html', context)


@login_required(login_url='adminlogin')
def admin_donation_view(request):
    donations = dmodels.BloodDonate.objects.all()
    return render(request, 'blood/admin_donation.html', {'donations': donations})


@login_required(login_url='adminlogin')
def update_approve_status_view(request, pk):
    req = models.BloodRequest.objects.get(id=pk)
    message = None
    bloodgroup = req.bloodgroup
    unit = req.unit
    stock = models.Stock.objects.get(bloodgroup=bloodgroup)
    if stock.unit > unit:
        stock.unit = stock.unit - unit
        stock.save()
        req.status = "Approved"

    else:
        message = "Stock Doest Not Have Enough Blood To Approve This Request, Only " + str(
            stock.unit) + " Unit Available"
    req.save()

    requests = models.BloodRequest.objects.all().filter(status='Pending')
    return render(request, 'blood/admin_request.html', {'requests': requests, 'message': message})


@login_required(login_url='adminlogin')
def update_reject_status_view(request, pk):
    req = models.BloodRequest.objects.get(id=pk)
    req.status = "Rejected"
    req.save()
    return HttpResponseRedirect('/admin-request')


@login_required(login_url='adminlogin')
def approve_donation_view(request, pk):
    donation = dmodels.BloodDonate.objects.get(id=pk)
    donation_blood_group = donation.bloodgroup
    donation_blood_unit = donation.unit

    stock = models.Stock.objects.get(bloodgroup=donation_blood_group)
    stock.unit = stock.unit + donation_blood_unit
    stock.save()

    donation.status = 'Approved'
    donation.save()
    return HttpResponseRedirect('/admin-donation')


@login_required(login_url='adminlogin')
def reject_donation_view(request, pk):
    donation = dmodels.BloodDonate.objects.get(id=pk)
    donation.status = 'Rejected'
    donation.save()
    return HttpResponseRedirect('/admin-donation')


@login_required(login_url='adminlogin')
def admin_volunteers_view(request):
    volunteers = amodels.VolunteerRegistration.objects.all()
    return render(request, 'blood/admin_volunteers.html', {'volunteers': volunteers})


@login_required(login_url='adminlogin')
def admin_blood_drives_view(request):
    # The Count function is used to get the number of volunteers in each BLoodDrives object
    blood_drives = models.BloodDrives.objects.annotate(no_of_volunteers=Count('volunteerregistration'))
    # blood_drives = models.BloodDrives.objects.all()
    hosted_drives = amodels.HostedBloodDrives.objects.all()
    # return render(request, 'blood/admin_blood.html')
    return render(request, 'blood/admin_blood_drives.html',
                  {'blood_drives': blood_drives, 'hosted_drives': hosted_drives})


def get_station_report(request):
    return render(request, 'blood/admin-dashboard.html')

def blood_request_view(request):
    request_form = forms.RequestForm()
    if request.method == 'POST':
        request_form = forms.RequestForm(request.POST, request.FILES)
        if request_form.is_valid():
            blood_request = request_form.save(commit=False)
            blood_request.blood_group = request_form.cleaned_data['blood_group']
            blood_request.save()

            messages.success(request, "Successfully submitted your blood request form. \n"
                                      "You will be redirected shortly")
            return render(request, 'blood/blood_request.html', {'request_form': request_form})
            time.sleep(1)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'blood/blood_request.html', {'request_form': request_form})
    return render(request, 'blood/blood_request.html', {'request_form': request_form})


def view_all_reports(request):
    donor_reports = vmodels.DonorReport.objects.all()
    donation_reports = vmodels.DonationReport.objects.all()
    return render(request, 'blood/admin_view_reports.html', {'donor_reports': donor_reports, 'donation_reports': donation_reports})


def create_campaign_view(request):
    campaign_form = forms.CampaignForm()

    if request.method == 'POST':
        campaign_form = forms.CampaignForm(request.POST, request.FILES)
        if campaign_form.is_valid():
            selected_counties = campaign_form.cleaned_data['county']
            print(f'Selected Counties: {selected_counties}')

            donors = []
            for county in selected_counties:
                donor = dmodels.Donor.objects.filter(county=county)
                if len(donor) > 0:
                    donors.extend(donor)

            print("Donors are" ,donors)
            if len(donors) >= 1:
                emails = []
                for donor in donors:
                    emails.append(donor.email)

                    # Add campaign notification to database
                    current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    notification = dmodels.Notifications(donor.donor_id,request.user,campaign_form.data['subject'], campaign_form.data['message'],"",current_date)
                    notification.save()

                print(emails)
                if len(emails) > 0:
                    string_email = ','.join(emails)
                    response = send_email_campaign(string_email,campaign_form)
                    if response != 'error':
                        messages.success(request, "Campaign Created Successfully")
                        return render(request, 'blood/create_campaign.html', {'campaign_form': campaign_form})
                    else:
                        messages.success(request, "Error in creating the campaign")
                        return render(request, 'blood/create_campaign.html', {'campaign_form': campaign_form})
            else:
                print("No Donors Found")
                return render(request, 'blood/create_campaign.html', {'campaign_form': campaign_form})

    return render(request, 'blood/create_campaign.html', {'campaign_form': campaign_form})