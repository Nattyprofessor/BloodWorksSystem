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


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = VolunteerRegistration
        fields = ['name', 'email', 'phone', 'location', 'reason']


class VolunteerRegistrationForm(forms.ModelForm):
    class Meta:
        model = VolunteerRegistration
        fields = ['name', 'email', 'phone', 'location', 'reason', 'blood_drive']

    def __init__(self, *args, **kwargs):
        location = kwargs.pop('location', '')
        super(VolunteerRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['blood_drive'] = forms.ModelChoiceField(queryset=BloodDrives.objects.filter(county=location))


class HostedBloodDrivesForm(forms.ModelForm):
    class Meta:
        model = HostedBloodDrives
        fields = ['name', 'organization', 'attendees', 'phone', 'email', 'address', 'county', 'date', 'plan_doc']
