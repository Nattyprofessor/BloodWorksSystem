from django.db import models
from django.contrib.auth.models import User
from blood.models import counties
from django.core.validators import RegexValidator


phoneNumberRegex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
# Create your models here.
# This model represents available appointment locations
class Appointment(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    map = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    image = models.URLField(
        default="https://i.seadn.io/gae/OGpebYaykwlc8Tbk-oGxtxuv8HysLYKqw-FurtYql2UBd_q_-ENAwDY82PkbNB68aTkCINn6tOhpA8pF5SAewC2auZ_44Q77PcOo870?auto=format&dpr=1&w=1000")
    status = models.CharField(max_length=20, default="Pending",
                              choices=[("Pending", "Pending"), ("Available", "Available"), ("Cancelled", "Cancelled")])

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add more fields as needed

    def __str__(self):
        return self.title


class Requests(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    location = models.ForeignKey(Appointment, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["location"]


# This model represents volunteering opportunities
# class Volunteering(models.Model):
#     title = models.CharField(max_length=100)
#     image = models.URLField(
#         default="https://i.seadn.io/gae/OGpebYaykwlc8Tbk-oGxtxuv8HysLYKqw-FurtYql2UBd_q_-ENAwDY82PkbNB68aTkCINn6tOhpA8pF5SAewC2auZ_44Q77PcOo870?auto=format&dpr=1&w=1000")
#     description = models.TextField()
#     date = models.DateField()
#     location = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.title
#
#
class VolunteerRegistration(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(validators=[phoneNumberRegex], unique=True, max_length=16)
    location = models.CharField(max_length=100, choices=counties)
    reason = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

class HostedBloodDrives(models.Model):
    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    attendees = models.PositiveIntegerField(max_length=100)
    phone = models.CharField(validators=[phoneNumberRegex], unique=True, max_length=16)
    email = models.EmailField()
    address = models.CharField(max_length=40)
    county = models.CharField(max_length=15, choices=counties)
    date = models.DateField()
    plan_doc = models.FileField(upload_to='hosted_blood_drives/',null=True, blank=True)

    def __str__(self):
        return self.organization
