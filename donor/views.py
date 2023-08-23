import datetime
import os

from django.shortcuts import render, redirect, reverse
from . import forms, models
from django.db.models import Sum, Q
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from datetime import date, timedelta
from django.core.mail import send_mail
from django.contrib.auth.models import User
from blood import forms as bforms
from blood import models as bmodels
from .functions import *


def donor_signup_view(request):
    userForm = forms.DonorUserForm()
    donorForm = forms.DonorForm()
    mydict = {'userForm': userForm, 'donorForm': donorForm}
    if request.method == 'POST':
        userForm = forms.DonorUserForm(request.POST)
        donorForm = forms.DonorProfileForm(request.POST, request.FILES)
        if userForm.is_valid() and donorForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            donor = donorForm.save(commit=False)
            donor.user = user
            #donor.bloodgroup = donorForm.cleaned_data['bloodgroup']
            donor.save()
            my_donor_group = Group.objects.get_or_create(name='DONOR')
            my_donor_group[0].user_set.add(user)

            user_name = user.first_name + " " + user.last_name
            # notify_admin_about_new_donor(donor, user_name)
            return HttpResponseRedirect('donorlogin')
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, userForm.errors)
            messages.error(request, donorForm.errors)

    return render(request, 'donor/donorsignup.html', context=mydict)


current_time = datetime.now().hour
print(current_time)


@login_required(login_url='/donor/donorlogin')
def donor_dashboard_view(request):
    donor = models.Donor.objects.get(user_id=request.user.id)
    try:
        health_info = models.DonorHealthInfo.objects.get(donor_id=donor.donor_id)
    except:
        health_info = None
    donation_history = list(models.BloodDonate.objects.filter(donor=donor.donor_id).values())
    user = models.User.objects.get(id=donor.user_id)
    # A new url is generated to download the card document in the event that the previous url expires
    print(datetime.now().hour, current_time)

    id_url = 'none'
    id_url = get_document_url(donor, donor.donor_card_code)

    # returns the most recent donation done by the user
    recent_date = find_most_recent_datetime(donation_history)
    print("The recent date is: ", recent_date)

    dict = {"donor": donor, "user": user, "id_url": id_url,
            'donation_history': len(donation_history),
            'recent_date': recent_date,
            'approved_donations': models.BloodDonate.objects.all().filter(donor=donor.donor_id).filter(
                status='Approved').count(),
            'rejected_donations': models.BloodDonate.objects.all().filter(donor=donor.donor_id).filter(
                status='Rejected').count(),
            'info': health_info,
            }
    return render(request, 'donor/donor_dashboard.html', context=dict)


def donation_history_view(request):
    donor = models.Donor.objects.get(user_id=request.user.id)
    donations = models.BloodDonate.objects.all().filter(donor=donor)
    return render(request, 'donor/donation_history.html', {'donations': donations})


def request_history_view(request):
    donor = models.Donor.objects.get(user_id=request.user.id)
    blood_request = bmodels.BloodRequest.objects.all().filter(request_by_donor=donor)
    return render(request, 'donor/request_history.html', {'blood_request': blood_request})


# Donor profile has been shifted to donor dashboard
# def donor_profile_view(request):
#     full_name = user.first_name + " " + user.last_name
#     return render(request, 'donor/donor_profile.html', context={"donor": donor, "user": user, "id_url": id_url})
def my_statements_view(request):
    donor = models.Donor.objects.get(user_id=request.user.id)


    directory = 'static/reports/donor-statements'
    search_string = donor.donor_id
    def search_files_with_string(directory, search_string):
        found_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if search_string in file:
                    found_files.append(os.path.join(root, file))
        return found_files

    statements = search_files_with_string(directory, search_string)
    if statements:
        return render(request, 'donor/donation_statements.html', {'reports': statements})
    messages.error(request,"You have no donation statements yet.")
    return render(request, 'donor/donation_statements.html')


def my_notifications_view(request):
    print(request.user.id)
    donor = models.Donor.objects.get(user_id=request.user.id)
    x = models.Notifications.objects.all().values()
    print(x)
    my_notifications = models.Notifications.objects.all().filter(donor=donor.donor_id)
    for index, notification in enumerate(my_notifications):
        group = notification.sender.groups.values_list('name', flat=True).first()
        print(group)
        my_notifications[index].group = group

    count = len(my_notifications)
    return render(request, 'donor/donor_notifications.html', {'notifications': my_notifications, 'count': count})


def my_pre_exams_view(request):
    donor = models.Donor.objects.get(user_id=request.user.id)
    donor_exams = models.PreExamInfo.objects.all().filter(donor_id  =donor.donor_id)

    if len(donor_exams) != 0:
        return render(request, 'donor/my_pre_exams.html', {'reports': donor_exams})
    messages.success(request, "You have no pre-exams yet.")
    return render(request, 'donor/my_pre_exams.html')
