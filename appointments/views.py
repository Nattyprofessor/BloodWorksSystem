from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import Appointment
from .forms import RequestForm


# Create your views here.
def main(request):
    appointments = Appointment.objects.all()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request has been submitted')
            return render(request, 'appointments/index.html', {'appointments': appointments, 'form': RequestForm(request.GET)})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
    else:
        form = RequestForm()
    return render(request, 'appointments/index.html', {'appointments': appointments, 'form': form})
