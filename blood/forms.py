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


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class CampaignForm(forms.Form):
    county = forms.MultipleChoiceField(choices=models.counties, required=True, widget=forms.CheckboxSelectMultiple)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    file_field = MultipleFileField(required=False)
