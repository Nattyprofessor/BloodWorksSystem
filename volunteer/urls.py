from django.urls import path

from django.contrib.auth.views import LoginView, PasswordResetView

import appointments
from . import views

urlpatterns = [
    path('registration', appointments.views.volunteer, name='volunteer'),
    path('volunteerlogin/', LoginView.as_view(template_name='volunteer/volunteer_login.html'),name='volunteerlogin'),
    path('volunteer-dashboard/', views.volunteer_dashboard_view, name='volunteer-dashboard'),
    path('update-donor/', views.search_donor, name='update-donor'),
    path('pre-exam/', views.pre_exam_view, name='pre-exam'),
    path('register-donor/', views.register_donor, name='register-donor'),
    path('donate-blood/', views.donate_blood_view, name='donate-blood'),
    path('donation-reports/', views.donation_reports_view, name="donation-reports"),
    path('donor-reports/', views.donor_reports_view, name="donor-reports"),
    path('generate-donation-report/', views.generate_donation_report, name="generate-donation-report"),
    path('generate-donor-report/', views.generate_donor_report, name="generate-donor-report"),
    path('generate-station-report/', views.generate_station_report, name="generate-station-report"),
    path('download-report/<str:pk>', views.download_report, name="download-report")

]


