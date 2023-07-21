from django.contrib import admin
from .models import *


# Register your models here.
class ReportsAdmin(admin.ModelAdmin):
    list_filter = ['station_id', 'created_at']
    search_fields = ['title']


admin.site.register(DonationReport, ReportsAdmin)
admin.site.register(DonorReport,ReportsAdmin)
admin.site.register(StationReport,ReportsAdmin)
