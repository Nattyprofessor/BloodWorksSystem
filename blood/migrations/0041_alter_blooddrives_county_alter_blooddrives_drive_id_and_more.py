# Generated by Django 4.2.3 on 2023-07-24 10:52

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0040_alter_blooddrives_county_alter_blooddrives_drive_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddrives',
            name='county',
            field=models.CharField(choices=[('Mombasa', 'Mombasa'), ('Samburu', 'Samburu'), ('Laikipia', 'Laikipia'), ('Uasin Gishu', 'Uasin Gishu'), ('Siaya', 'Siaya'), ('Lamu', 'Lamu'), ('Vihiga', 'Vihiga'), ('Tana River', 'Tana River'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Kwale', 'Kwale'), ('Mandera', 'Mandera'), ('Kitui', 'Kitui'), ('Makueni', 'Makueni'), ('Kisii', 'Kisii'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Baringo', 'Baringo'), ('Narok', 'Narok'), ('Embu', 'Embu'), ('Kilifi', 'Kilifi'), ('Nyandarua', 'Nyandarua'), ('Kisumu', 'Kisumu'), ('Nandi', 'Nandi'), ("Murang'a", "Murang'a"), ('Taita-Taveta', 'Taita-Taveta'), ('Bungoma', 'Bungoma'), ('Meru', 'Meru'), ('Kirinyaga', 'Kirinyaga'), ('Bomet', 'Bomet'), ('Kiambu', 'Kiambu'), ('Homa Bay', 'Homa Bay'), ('Machakos', 'Machakos'), ('Garissa', 'Garissa'), ('Isiolo', 'Homa Bay'), ('Kakamega', 'Kakamega'), ('Busia', 'Busia'), ('Kericho', 'Kericho'), ('Kajiado', 'Kajiado'), ('Trans Nzoia', 'Trans Nzoia'), ('Migori', 'Migori'), ('Nairobi', 'Nairobi'), ('Marsabit', 'Marsabit'), ('Turkana', 'Turkana'), ('Wajir', 'Wajir'), ('West Pokot', 'West Pokot'), ('Nyamira', 'Nyamira'), ('Nakuru', 'Nakuru'), ('Nyeri', 'Nyeri')], max_length=15),
        ),
        migrations.AlterField(
            model_name='blooddrives',
            name='drive_id',
            field=models.CharField(default=uuid.UUID('94ecd7d3-15ec-4ea9-a285-ff15f9313458'), max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bloodrequest',
            name='blood_group',
            field=models.CharField(choices=[('O+', 'O+'), ('AB+', 'AB+'), ('A', 'A'), ('B-', 'B-'), ('O-', 'O-'), ('A+', 'A+'), ('B+', 'B+'), ('AB-', 'AB-')], default='None', max_length=10),
        ),
        migrations.AlterField(
            model_name='bloodrequest',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 24, 13, 52, 36, 514957)),
        ),
        migrations.AlterField(
            model_name='bloodrequest',
            name='status',
            field=models.CharField(choices=[('Rejected', 'Rejected'), ('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=20),
        ),
    ]