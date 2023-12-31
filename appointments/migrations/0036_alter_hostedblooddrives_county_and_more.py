# Generated by Django 4.2.3 on 2023-07-17 20:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0035_alter_hostedblooddrives_county_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostedblooddrives',
            name='county',
            field=models.CharField(choices=[('Garissa', 'Garissa'), ('Bomet', 'Bomet'), ('Baringo', 'Baringo'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Bungoma', 'Bungoma'), ('Makueni', 'Makueni'), ("Murang'a", 'Murang'), ('Nakuru', 'Nakuru'), ('Nyamira', 'Nyamira'), ('Uasin Gishu', 'Uasin Gishu'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Laikipia', 'Laikipia'), ('Migori', 'Migori'), ('Turkana', 'Turkana'), ('Nyandarua', 'Nyandarua'), ('Meru', 'Meru'), ('Siaya', 'Siaya'), ('Lamu', 'Lamu'), ('Taita-Taveta', 'Taita-Taveta'), ('Kilifi', 'Kilifi'), ('Vihiga', 'Vihiga'), ('Kitui', 'Kitui'), ('Kakamega', 'Kakamega'), ('Kajiado', 'Kajiado'), ('Tana River', 'Tana River'), ('Nairobi', 'Nairobi'), ('Busia', 'Busia'), ('West Pokot', 'West Pokot'), ('Kisumu', 'Kisumu'), ('Wajir', 'Wajir'), ('Narok', 'Narok'), ('Marsabit', 'Marsabit'), ('Nandi', 'Nandi'), ('Homa Bay', 'Homa Bay'), ('Nyeri', 'Nyeri'), ('Mombasa', 'Mombasa'), ('Samburu', 'Samburu'), ('Kirinyaga', 'Kirinyaga'), ('Mandera', 'Mandera'), ('Embu', 'Embu'), ('Machakos', 'Machakos'), ('Kiambu', 'Kiambu'), ('Isiolo', 'Homa Bay'), ('Kwale', 'Kwale'), ('Kisii', 'Kisii'), ('Kericho', 'Kericho'), ('Trans Nzoia', 'Trans Nzoia')], max_length=15),
        ),
        migrations.AlterField(
            model_name='volunteerregistration',
            name='location',
            field=models.CharField(choices=[('Garissa', 'Garissa'), ('Bomet', 'Bomet'), ('Baringo', 'Baringo'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Bungoma', 'Bungoma'), ('Makueni', 'Makueni'), ("Murang'a", 'Murang'), ('Nakuru', 'Nakuru'), ('Nyamira', 'Nyamira'), ('Uasin Gishu', 'Uasin Gishu'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Laikipia', 'Laikipia'), ('Migori', 'Migori'), ('Turkana', 'Turkana'), ('Nyandarua', 'Nyandarua'), ('Meru', 'Meru'), ('Siaya', 'Siaya'), ('Lamu', 'Lamu'), ('Taita-Taveta', 'Taita-Taveta'), ('Kilifi', 'Kilifi'), ('Vihiga', 'Vihiga'), ('Kitui', 'Kitui'), ('Kakamega', 'Kakamega'), ('Kajiado', 'Kajiado'), ('Tana River', 'Tana River'), ('Nairobi', 'Nairobi'), ('Busia', 'Busia'), ('West Pokot', 'West Pokot'), ('Kisumu', 'Kisumu'), ('Wajir', 'Wajir'), ('Narok', 'Narok'), ('Marsabit', 'Marsabit'), ('Nandi', 'Nandi'), ('Homa Bay', 'Homa Bay'), ('Nyeri', 'Nyeri'), ('Mombasa', 'Mombasa'), ('Samburu', 'Samburu'), ('Kirinyaga', 'Kirinyaga'), ('Mandera', 'Mandera'), ('Embu', 'Embu'), ('Machakos', 'Machakos'), ('Kiambu', 'Kiambu'), ('Isiolo', 'Homa Bay'), ('Kwale', 'Kwale'), ('Kisii', 'Kisii'), ('Kericho', 'Kericho'), ('Trans Nzoia', 'Trans Nzoia')], max_length=100),
        ),
        migrations.AlterField(
            model_name='volunteerregistration',
            name='volunteer_id',
            field=models.CharField(default=uuid.UUID('81d77a4c-f0a1-44dd-ae22-620d16c308c8'), max_length=20, primary_key=True, serialize=False),
        ),
    ]
