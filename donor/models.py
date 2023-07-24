import datetime
import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from appointments.models import VolunteerRegistration
from blood.models import counties

blood_groups = {('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A', 'A'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'),
                ('AB-', 'AB-')}
donation_types = {('Plasma', 'Plasma'), ('Blood', 'Blood'), ('Platelets', 'Platelets'), ('Power Red', 'Power Red')}


class Donor(models.Model):
    current_time = datetime.datetime.now()

    donor_id = models.CharField(primary_key=True, max_length=40, default=uuid.uuid4())
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/Donor/', default="profile/Donor/default.png", null=True,
                                    blank=True)
    bloodgroup = models.CharField(max_length=10, choices=blood_groups)
    address = models.CharField(max_length=40)
    county = models.CharField(max_length=15, default="None", choices=counties)
    mobile = models.CharField(max_length=20, null=False, unique=True)
    email = models.EmailField(default="test@placeholder.com")
    status = models.CharField(max_length=8, default="Pending",
                              choices={('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')})
    donor_card_code = models.CharField(max_length=40, null=True, blank=True)
    served_by = models.ForeignKey(VolunteerRegistration, null=True, default="delete-101", on_delete=models.SET_DEFAULT,
                                  blank=True)
    created_date = models.DateTimeField(auto_now_add=False, default=timezone.datetime.now())

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return f"{self.user.first_name}-{self.donor_id}"

    def json(self):
        return {
            'donor_id': self.donor_id,
            'donor_name': f'{self.get_name}',
            'card_code': self.donor_card_code,
            'address': self.address,
            'mobile': self.mobile,
            'email': self.email,
            'status': self.status
        }


class DonorHealthInfo(models.Model):
    donor_id = models.OneToOneField(Donor, on_delete=models.CASCADE)
    taken_on = models.DateTimeField(auto_now=False, blank=True)
    blood_group = models.CharField(choices=blood_groups, max_length=3, null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    gender = models.CharField(max_length=3, default='Nil', choices={('M', 'M'), ('F', 'F'), ('Nil', 'Nil')})
    next_safe_date = models.DateField(blank=True)

    def __str__(self):
        return str(self.donor_id)


class PreExamInfo(models.Model):
    donor_id = models.ForeignKey(Donor, on_delete=models.CASCADE, blank=True, null=True)
    volunteer_id = models.ForeignKey(VolunteerRegistration, null=True, blank=True, default="delete-101",
                                     on_delete=models.SET_DEFAULT)
    pre_exam_id = models.CharField(primary_key=True, max_length=10, default=uuid.uuid4())
    haemoglobin_gDL = models.DecimalField(max_digits=5, decimal_places=2)
    temperature_C = models.DecimalField(max_digits=5, decimal_places=2)
    blood_pressure = models.CharField(max_length=10, default='0/0')
    pulse_rate_BPM = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=8, default="Pending",
                              choices={('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')})
    created_date = models.DateTimeField(auto_now=False, default=timezone.datetime.now())

    def __str__(self):
        return str(self.donor_id)


class DonationType(models.Model):
    type = models.CharField(default='Blood', max_length=10, choices=donation_types)
    no_of_donations = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.type)


class BloodDonate(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    donation_id = models.CharField(primary_key=True, default=uuid.uuid4(), max_length=40)
    volunteer_id = models.ForeignKey(VolunteerRegistration, null=True, on_delete=models.SET_NULL)
    disease = models.CharField(max_length=100, default="Nothing")
    age = models.PositiveIntegerField()
    blood_group = models.CharField(max_length=3, blank=True, choices=blood_groups)
    donation_type = models.ForeignKey(DonationType, default=1, on_delete=models.CASCADE)
    unit = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, default="Pending",
                              choices={('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')})
    created_date = models.DateTimeField(auto_now=False, default=timezone.datetime.now())

    def __str__(self):
        return f'{self.donor.user.first_name}-{self.donation_id}'

    def json(self, volunteer_id):

        if volunteer_id == self.volunteer_id.volunteer_id:
            return {
                'donor_id': self.donor.donor_id,
                'donor_name': f'{self.donor.user.first_name}',
                'units': self.unit,
                'blood_group': self.blood_group,
                'donation_type': self.donation_type.type
            }
        else:
            return {}


class Notifications(models.Model):
    #notification_id = models.CharField(max_length=100, primary_key=True, default=f'notification-{uuid.uuid4()}')
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='Title')
    message = models.CharField(max_length=500, null=True, blank=True)
    attachment = models.URLField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now=False, default=timezone.datetime.now())

    def __str__(self):
        return str(f'{self.title}-{self.created_date}')
