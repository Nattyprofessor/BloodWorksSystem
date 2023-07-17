from django.shortcuts import render, redirect, reverse
from . import forms, models
from django.db.models import Sum, Q
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
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
        donorForm = forms.DonorForm(request.POST, request.FILES)
        if userForm.is_valid() and donorForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            donor = donorForm.save(commit=False)
            donor.user = user
            donor.bloodgroup = donorForm.cleaned_data['bloodgroup']
            donor.save()
            my_donor_group = Group.objects.get_or_create(name='DONOR')
            my_donor_group[0].user_set.add(user)

            user_name = user.first_name + " " + user.last_name
            notify_admin_about_new_donor(donor,user_name)

        return HttpResponseRedirect('donorlogin')
    return render(request, 'donor/donorsignup.html', context=mydict)


def donor_dashboard_view(request):
    donor = models.Donor.objects.get(user_id=request.user.id)
    dict = {
        'requestpending': bmodels.BloodRequest.objects.all().filter(request_by_donor=donor).filter(
            status='Pending').count(),
        'requestapproved': bmodels.BloodRequest.objects.all().filter(request_by_donor=donor).filter(
            status='Approved').count(),
        'requestmade': bmodels.BloodRequest.objects.all().filter(request_by_donor=donor).count(),
        'requestrejected': bmodels.BloodRequest.objects.all().filter(request_by_donor=donor).filter(
            status='Rejected').count(),
    }
    return render(request, 'donor/donor_dashboard.html', context=dict)


def donation_history_view(request):
    donor = models.Donor.objects.get(user_id=request.user.id)
    donations = models.BloodDonate.objects.all().filter(donor=donor)
    return render(request, 'donor/donation_history.html', {'donations': donations})


def make_request_view(request):
    request_form = bforms.RequestForm()
    if request.method == 'POST':
        request_form = bforms.RequestForm(request.POST)
        if request_form.is_valid():
            blood_request = request_form.save(commit=False)
            blood_request.bloodgroup = request_form.cleaned_data['bloodgroup']
            donor = models.Donor.objects.get(user_id=request.user.id)
            blood_request.request_by_donor = donor
            blood_request.save()
            return HttpResponseRedirect('request-history')
    return render(request, 'donor/makerequest.html', {'request_form': request_form})


def request_history_view(request):
    donor = models.Donor.objects.get(user_id=request.user.id)
    blood_request = bmodels.BloodRequest.objects.all().filter(request_by_donor=donor)
    return render(request, 'donor/request_history.html', {'blood_request': blood_request})


def donor_profile_view(request):
    donor = models.Donor.objects.get(user_id=request.user.id)
    user = models.User.objects.get(id=donor.user_id)

    full_name = user.first_name + " " + user.last_name

    # A new url is generated to download the card document in the event that the previous url expires
    id_url = get_document_url(donor.donor_card_code)

    return render(request, 'donor/donor_profile.html', context={"donor": donor, "user": user, "id_url": id_url})
