from django import forms
from django.contrib.auth.models import User
from . import models


class DonorUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class DonorForm(forms.ModelForm):
    class Meta:
        model = models.Donor
        fields = ['status', 'bloodgroup', 'address', 'mobile', 'email', 'profile_pic']


class SearchDonor(forms.Form):
    search_donor = forms.CharField()


class DonorHealthForm(forms.ModelForm):
    class Meta:
        model = models.DonorHealthInfo
        fields = ['donor_id', 'taken_on', 'blood_group', 'height', 'weight', 'gender', 'next_safe_date']


class DateInput(forms.DateInput):
    input_type = 'date'


class DonationForm(forms.ModelForm):
    class Meta:
        model = models.BloodDonate
        fields = ['volunteer_id', 'donation_id', 'donor', 'age', 'blood_group', 'disease', 'unit', 'donation_type',
                  'status', 'created_date']
        widgets = {'created_date': DateInput()}


class PreExamForm(forms.ModelForm):
    class Meta:
        model = models.PreExamInfo
        fields = ['donor_id', 'haemoglobin_gDL', 'temperature_C', 'blood_pressure', 'pulse_rate_BPM']
