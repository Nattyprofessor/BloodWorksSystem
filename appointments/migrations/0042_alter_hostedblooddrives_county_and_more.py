# Generated by Django 4.2.3 on 2023-07-24 06:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0041_alter_hostedblooddrives_county_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostedblooddrives',
            name='county',
            field=models.CharField(choices=[('West Pokot', 'West Pokot'), ('Embu', 'Embu'), ('Siaya', 'Siaya'), ('Busia', 'Busia'), ('Kirinyaga', 'Kirinyaga'), ('Garissa', 'Garissa'), ('Machakos', 'Machakos'), ('Kwale', 'Kwale'), ('Kisii', 'Kisii'), ('Narok', 'Narok'), ('Uasin Gishu', 'Uasin Gishu'), ('Taita-Taveta', 'Taita-Taveta'), ('Nyeri', 'Nyeri'), ('Meru', 'Meru'), ('Kakamega', 'Kakamega'), ('Vihiga', 'Vihiga'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Laikipia', 'Laikipia'), ('Wajir', 'Wajir'), ('Nyamira', 'Nyamira'), ('Trans Nzoia', 'Trans Nzoia'), ('Kitui', 'Kitui'), ('Makueni', 'Makueni'), ('Kiambu', 'Kiambu'), ('Turkana', 'Turkana'), ('Samburu', 'Samburu'), ('Bungoma', 'Bungoma'), ('Bomet', 'Bomet'), ("Murang'a", 'Murang'), ('Kericho', 'Kericho'), ('Kilifi', 'Kilifi'), ('Kajiado', 'Kajiado'), ('Nyandarua', 'Nyandarua'), ('Mombasa', 'Mombasa'), ('Lamu', 'Lamu'), ('Isiolo', 'Homa Bay'), ('Nakuru', 'Nakuru'), ('Nandi', 'Nandi'), ('Nairobi', 'Nairobi'), ('Migori', 'Migori'), ('Kisumu', 'Kisumu'), ('Baringo', 'Baringo'), ('Homa Bay', 'Homa Bay'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Marsabit', 'Marsabit'), ('Mandera', 'Mandera'), ('Tana River', 'Tana River')], max_length=15),
        ),
        migrations.AlterField(
            model_name='volunteerregistration',
            name='location',
            field=models.CharField(choices=[('West Pokot', 'West Pokot'), ('Embu', 'Embu'), ('Siaya', 'Siaya'), ('Busia', 'Busia'), ('Kirinyaga', 'Kirinyaga'), ('Garissa', 'Garissa'), ('Machakos', 'Machakos'), ('Kwale', 'Kwale'), ('Kisii', 'Kisii'), ('Narok', 'Narok'), ('Uasin Gishu', 'Uasin Gishu'), ('Taita-Taveta', 'Taita-Taveta'), ('Nyeri', 'Nyeri'), ('Meru', 'Meru'), ('Kakamega', 'Kakamega'), ('Vihiga', 'Vihiga'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Laikipia', 'Laikipia'), ('Wajir', 'Wajir'), ('Nyamira', 'Nyamira'), ('Trans Nzoia', 'Trans Nzoia'), ('Kitui', 'Kitui'), ('Makueni', 'Makueni'), ('Kiambu', 'Kiambu'), ('Turkana', 'Turkana'), ('Samburu', 'Samburu'), ('Bungoma', 'Bungoma'), ('Bomet', 'Bomet'), ("Murang'a", 'Murang'), ('Kericho', 'Kericho'), ('Kilifi', 'Kilifi'), ('Kajiado', 'Kajiado'), ('Nyandarua', 'Nyandarua'), ('Mombasa', 'Mombasa'), ('Lamu', 'Lamu'), ('Isiolo', 'Homa Bay'), ('Nakuru', 'Nakuru'), ('Nandi', 'Nandi'), ('Nairobi', 'Nairobi'), ('Migori', 'Migori'), ('Kisumu', 'Kisumu'), ('Baringo', 'Baringo'), ('Homa Bay', 'Homa Bay'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Marsabit', 'Marsabit'), ('Mandera', 'Mandera'), ('Tana River', 'Tana River')], max_length=100),
        ),
        migrations.AlterField(
            model_name='volunteerregistration',
            name='volunteer_id',
            field=models.CharField(default=uuid.UUID('f625a40e-2660-4638-8a3c-542c979962c4'), max_length=20, primary_key=True, serialize=False),
        ),
    ]
