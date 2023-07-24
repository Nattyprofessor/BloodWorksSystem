from django.contrib import admin
from .models import Donor,DonorHealthInfo,DonationType, PreExamInfo, BloodDonate, Notifications
# Register your models here.
admin.site.register(Donor)
admin.site.register(DonorHealthInfo)
admin.site.register(DonationType)
admin.site.register(PreExamInfo)
admin.site.register(BloodDonate)
admin.site.register(Notifications)