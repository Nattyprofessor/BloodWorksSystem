"""bloodbankmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include

from appointments import views as a_views
from blood import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('tutorial/', include('tutorial.urls')),
    path('donor/', include('donor.urls')),
    path('patient/', include('patient.urls')),
    path('volunteer/', include('volunteer.urls')),

    path('create_appointment/', a_views.main, name='create_appointment'),
    path('blood_drives/', a_views.show_drives, name='blood_drives'),

    path('host-blood-drive/', a_views.host_blood_drive, name='host-blood-drive'),
    path('blood_request/', views.blood_request_view, name='blood_request'),

    path('', views.home_view, name=''),
    path('logout', LogoutView.as_view(template_name='blood/logout.html'), name='logout'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    path('adminlogin', LoginView.as_view(template_name='blood/adminlogin.html'), name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view, name='admin-dashboard'),
    path('admin-blood', views.admin_blood_view, name='admin-blood'),
    path('admin-donor', views.admin_donor_view, name='admin-donor'),
    path('admin-patient', views.admin_patient_view, name='admin-patient'),
    path('admin-volunteers', views.admin_volunteers_view, name='admin-volunteers'),
    path('admin-blood-drives', views.admin_blood_drives_view, name='admin-blood-drives'),
    path('update-donor/<str:id>', views.update_donor_view, name='update-donor'),
    path('assign-volunteer/<str:id>', views.assign_volunteer_view, name='assign-volunteer'),
    path('reject-volunteer/<str:id>', views.reject_volunteer_view, name='reject-volunteer'),
    path('delete-donor/<str:pk>', views.delete_donor_view, name='delete-donor'),
    path('admin-request', views.admin_request_view, name='admin-request'),
    path('admin-appointment', views.admin_show_appointments_view, name='admin-appointment'),
    path('update-patient/<int:pk>', views.update_patient_view, name='update-patient'),
    path('delete-patient/<int:pk>', views.delete_patient_view, name='delete-patient'),
    path('admin-donation', views.admin_donation_view, name='admin-donation'),
    path('approve-donation/<str:pk>/<str:pos>', views.approve_donation_view, name='approve-donation'),
    path('reject-donation/<str:pk>/<str:pos>', views.reject_donation_view, name='reject-donation'),
    path('admin-request-history', views.admin_request_history_view, name='admin-request-history'),
    path('update-approve-status/<int:pk>', views.update_approve_status_view, name='update-approve-status'),
    path('update-reject-status/<int:pk>', views.update_reject_status_view, name='update-reject-status'),
    path('view-all-reports', views.view_all_reports, name='view-all-reports'),
    path('get-station-report', views.get_station_report, name='get-station-report'),
    path('create-campaign', views.create_campaign_view, name='create-campaign'),

]
