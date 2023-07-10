from django.shortcuts import render
from django.http import HttpResponse
from .models import Appointment
# Create your views here.
def main(request):
    appointments = Appointment.objects.all()
    return render(request,'appointments/index.html',{'appointments':appointments})
