from django import forms

from .models import *


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['title', 'date', 'time', 'map', 'email', 'phone']


class RequestForm(forms.ModelForm):
    class Meta:
        model = Requests
        fields = ['name', 'email', 'phone', 'location']


class VolunteerRegistrationForm(forms.ModelForm):
    class Meta:
        model = VolunteerRegistration
        fields = ['name', 'email', 'phone', 'location', 'reason']


class HostedBloodDrivesForm(forms.ModelForm):
    class Meta:
        model = HostedBloodDrives
        fields = ['name', 'organization', 'attendees', 'phone', 'email', 'address', 'county', 'date', 'plan_doc']
