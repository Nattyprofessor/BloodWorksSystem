from django.urls import path

from django.contrib.auth.views import LoginView, PasswordResetView
from . import views
urlpatterns = [
    path('donorlogin', LoginView.as_view(template_name='donor/donorlogin.html'),name='donorlogin'),
    path('donorforgot', PasswordResetView.as_view(template_name='donor/forgot.html'),name='donorforgot' ),
    path('donorsignup', views.donor_signup_view,name='donorsignup'),
    path('donor-dashboard', views.donor_dashboard_view,name='donor-dashboard'),
    #path('donor-profile', views.donor_profile_view, name='donor-profile'),
    # path('donate-blood', views.donate_blood_view,name='donate-blood'), Moved to volunteer app view
    path('donation-history', views.donation_history_view,name='donation-history'),
    path('request-history', views.request_history_view,name='request-history'),
    path('my-statements', views.my_statements_view,name='my-statements'),
    path('my-notifications', views.my_notifications_view,name='my-notifications'),
    path('my-pre-exams', views.my_pre_exams_view,name='my-pre-exams'),
]