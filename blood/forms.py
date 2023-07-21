from django import forms

from . import models


class BloodForm(forms.ModelForm):
    class Meta:
        model = models.Stock
        fields = ['bloodgroup', 'unit']


class RequestForm(forms.ModelForm):
    class Meta:
        model = models.BloodRequest
        fields = ['patient_name', 'patient_age', 'reason', 'email', 'blood_group', 'id_f_photo', 'id_b_photo',
                  'document', 'referred_person', 'referral_mobile', 'date', 'status', 'blood_group', 'unit']
