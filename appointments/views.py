from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages

from blood.models import BloodDrives
from .models import Appointment
from .forms import RequestForm, VolunteerRegistrationForm, HostedBloodDrivesForm
from .functions import handle_uploaded_file

# Create your views here.
def main(request):
    appointments = Appointment.objects.all()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request has been submitted')
            return render(request, 'appointments/appointments.html',
                          {'appointments': appointments, 'form': RequestForm(request.GET)})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    else:
        form = RequestForm()
    return render(request, 'appointments/appointments.html', {'appointments': appointments, 'form': form})


def show_drives(request):
    drives = BloodDrives.objects.all()

    for x in drives:
        date = x.get_date()
        setattr(x, 'day', date[0])
        setattr(x, 'month', date[1])
        print(x.day)

    return render(request, 'appointments/blood_drives.html', {'blood_drives': drives})


def volunteer(request):
    if request.method == 'POST':
        form = VolunteerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for registering')
            return render(request, 'appointments/volunteer.html',
                          {'form': VolunteerRegistrationForm(request.GET)})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    else:
        form = VolunteerRegistrationForm()

    return render(request, 'appointments/volunteer.html', {'form': form})


def host_blood_drive(request):
    form = HostedBloodDrivesForm()
    if request.method == 'POST':
        registration_form = HostedBloodDrivesForm(request.POST, request.FILES)
        if registration_form.is_valid():
            #handle_uploaded_file(registration_form.cleaned_data['name'], request.FILES['plan_doc'])
            #messages.success(request, 'Document uploaded successfully.')
            registration_form.save()
            messages.success(request, 'Thank you for registering')

            return render(request, 'appointments/host_blood_drive.html',
                          {'form': HostedBloodDrivesForm(request.GET)})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, registration_form.errors)

    return render(request, 'appointments/host_blood_drive.html', {'form': form})
