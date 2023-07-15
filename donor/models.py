from django.db import models
from django.contrib.auth.models import User

blood_groups = {('O+', 'O+'),('O-', 'O-'),('A+', 'A+'),('A', 'A'),('B+', 'B+'),('B-', 'B-'),('AB+', 'AB+'),('AB-', 'AB-')}
class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/Donor/', null=True, blank=True)
    bloodgroup = models.CharField(max_length=10, choices=blood_groups)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False,unique=True)
    email = models.EmailField(default="test@placeholder.com")
    status = models.CharField(max_length=8, default="Pending",
                              choices={('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')})
    donor_card_code = models.CharField(max_length=40,null=True, blank=True)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.user.first_name


class BloodDonate(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    disease = models.CharField(max_length=100, default="Nothing")
    age = models.PositiveIntegerField()
    bloodgroup = models.CharField(max_length=10)
    unit = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, default="Pending")
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.donor
