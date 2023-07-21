import uuid

from django.db import models
from appointments.models import VolunteerRegistration


class DonationReport(models.Model):
    volunteer = models.ForeignKey(VolunteerRegistration, on_delete=models.CASCADE)
    report_id = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4())
    station_id = models.CharField(max_length=50, null=True, default="x")
    title = models.CharField(max_length=100, default='Donation-report')
    file = models.FileField(upload_to='reports/donation-reports/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=False)

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.report_id


class DonorReport(models.Model):
    volunteer = models.ForeignKey(VolunteerRegistration, on_delete=models.CASCADE)
    report_id = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4())
    station_id = models.CharField(max_length=50, null=True, default="x")
    title = models.CharField(max_length=100, default='Donation-report')
    file = models.FileField(upload_to='reports/donor-reports/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=False)

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.report_id

class StationReport(models.Model):
    volunteer = models.ForeignKey(VolunteerRegistration, on_delete=models.CASCADE)
    report_id = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4())
    station_id = models.CharField(max_length=50, null=True, default="x")
    title = models.CharField(max_length=100, default='Station-report')
    file = models.FileField(upload_to='reports/station-reports/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=False)

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.report_id