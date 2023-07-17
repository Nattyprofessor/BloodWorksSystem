import uuid

from django.db import models

from patient import models as pmodels

# All counties in Kenya
counties = {
    ("Baringo", "Baringo"),
    ("Bomet", "Bomet"),
    ("Bungoma", "Bungoma"),
    ("Busia", "Busia"),
    ("Elgeyo-Marakwet", "Elgeyo-Marakwet"),
    ("Embu", "Embu"),
    ("Garissa", "Garissa"),
    ("Homa Bay", "Homa Bay"),
    ("Isiolo", "Homa Bay"),
    ("Kajiado", "Kajiado"),
     ("Kakamega", "Kakamega"),
     ("Kericho", "Kericho"),
     ("Kiambu", "Kiambu"),
    ("Kilifi", "Kilifi"),
     ("Kirinyaga", "Kirinyaga"),
    ("Kisii", "Kisii"),
     ("Kisumu", "Kisumu"),
     ("Kitui", "Kitui"),
     ("Kwale", "Kwale"),
     ("Laikipia", "Laikipia"),
     ("Lamu", "Lamu"),
    ("Machakos", "Machakos"),
     ("Makueni", "Makueni"),
     ("Mandera", "Mandera"),
     ("Marsabit", "Marsabit"),
     ("Meru", "Meru"),
     ("Migori", "Migori"),
     ("Mombasa", "Mombasa"),
     ("Murang'a", "Murang"),
     ("Nairobi", "Nairobi"),
     ("Nakuru", "Nakuru"),
     ("Nandi", "Nandi"),
     ("Narok", "Narok"),
     ("Nyamira", "Nyamira"),
     ("Nyandarua", "Nyandarua"),
     ("Nyeri", "Nyeri"),
     ("Samburu", "Samburu"),
     ("Siaya", "Siaya"),
     ("Taita-Taveta", "Taita-Taveta"),
     ("Tana River", "Tana River"),
     ("Tharaka-Nithi", "Tharaka-Nithi"),
     ("Trans Nzoia", "Trans Nzoia"),
    ("Turkana", "Turkana"),
     ("Uasin Gishu", "Uasin Gishu"),
     ("Vihiga", "Vihiga"),
     ("Wajir", "Wajir"),
     ("West Pokot", "West Pokot")
}


location_codes = {
    "BWF", "Blood Works Facility",
    "BDHS", "Blood Drive - High School",
    "BDUN", "Blood Drive - University",
    "HSP", "Hospital",
    "MILT", "Military Facility",
    "MBD", "Mobile Blood Drive",
    "CLIN", "Clinic",
}


class Stock(models.Model):
    bloodgroup = models.CharField(max_length=10)
    unit = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.bloodgroup


class BloodRequest(models.Model):
    request_by_patient = models.ForeignKey(pmodels.Patient, null=True, on_delete=models.CASCADE)
    #request_by_donor = models.ForeignKey(dmodels.Donor, null=True, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=30)
    patient_age = models.PositiveIntegerField()
    reason = models.CharField(max_length=500)
    bloodgroup = models.CharField(max_length=10)
    unit = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, default="Pending")
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.bloodgroup


class LocationCodes(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    description = models.CharField(max_length=100)


# This model contains all blood drives in all counties in the country
class BloodDrives(models.Model):
    drive_id = models.CharField(primary_key=True,default=uuid.uuid4(), max_length=20)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=40)
    county = models.CharField(max_length=15, choices=counties)
    location_code = models.ForeignKey(LocationCodes, on_delete=models.CASCADE)
    date = models.DateField()
    #volunteer_count = models.PositiveIntegerField
    #volunteers = models.ManyToManyField(VolunteerRegistration, related_name="blood_drive")
    def __str__(self):
        return self.name

    def get_date(self):
        return [self.date.strftime('%d'), self.date.strftime('%b'), self.date.strftime('%Y')]
