from django.contrib import admin
from .models import *
import secrets

counties = {
    "Baringo": "BR",
    "Bomet": "BM",
    "Bungoma": "BG",
    "Busia": "BS",
    "Elgeyo-Marakwet": "EM",
    "Embu": "EB",
    "Garissa": "GA",
    "Homa Bay": "HB",
    "Isiolo": "IS",
    "Kajiado": "KJ",
    "Kakamega": "KK",
    "Kericho": "KR",
    "Kiambu": "KB",
    "Kilifi": "KF",
    "Kirinyaga": "KY",
    "Kisii": "KI",
    "Kisumu": "KM",
    "Kitui": "KT",
    "Kwale": "KW",
    "Laikipia": "LP",
    "Lamu": "LM",
    "Machakos": "MC",
    "Makueni": "MK",
    "Mandera": "MD",
    "Marsabit": "MB",
    "Meru": "ME",
    "Migori": "MG",
    "Mombasa": "MM",
    "Murang'a": "MR",
    "Nairobi": "NRB",
    "Nakuru": "NU",
    "Nandi": "ND",
    "Narok": "NR",
    "Nyamira": "NYA",
    "Nyandarua": "NN",
    "Nyeri": "NY",
    "Samburu": "SB",
    "Siaya": "SY",
    "Taita-Taveta": "TT",
    "Tana River": "TR",
    "Tharaka-Nithi": "THN",
    "Trans Nzoia": "TN",
    "Turkana": "TK",
    "Uasin Gishu": "UG",
    "Vihiga": "VG",
    "Wajir": "WJ",
    "West Pokot": "WP"
}

# Register your models here.
admin.site.register(LocationCodes)
admin.site.register(Stock)
admin.site.register(BloodRequest)


def generate_drive_id(location_code, county):
    county_code = counties.get(county)
    num = secrets.randbelow(10000)
    return f'{county_code}-{location_code}-{num}'


class BloodDrivesAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'name', 'address', 'county', 'location_code', 'date')
    list_filter = ['county', 'location_code']
    search_fields = ['name']

    # exclude = ['title_gen', 'Playlist', 'Tags', 'deleted', 'author', 'Category', 'Language']

    class Meta:
        model = BloodDrives

    # def get_queryset(self, request):
    #     return self.model.all_objects.all()

    def save_model(self, request, obj, form, change):
        print(obj.location_code.code)
        obj.save()

        if not change:
            x_id = generate_drive_id(obj.location_code.code, obj.county)
            obj.drive_id = x_id
            obj.save(update_fields=['drive_id'])
            print('done')


admin.site.register(BloodDrives, BloodDrivesAdmin)
