from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Appointment(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    map = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    image = models.URLField(
        default="https://i.seadn.io/gae/OGpebYaykwlc8Tbk-oGxtxuv8HysLYKqw-FurtYql2UBd_q_-ENAwDY82PkbNB68aTkCINn6tOhpA8pF5SAewC2auZ_44Q77PcOo870?auto=format&dpr=1&w=1000")

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
