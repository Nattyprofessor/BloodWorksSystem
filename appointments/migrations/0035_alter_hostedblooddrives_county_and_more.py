# Generated by Django 4.2.3 on 2023-07-17 17:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0034_alter_hostedblooddrives_county_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostedblooddrives',
            name='county',
            field=models.CharField(choices=[('Vihiga', 'Vihiga'), ('Bomet', 'Bomet'), ('Kiambu', 'Kiambu'), ('Siaya', 'Siaya'), ('Meru', 'Meru'), ('Trans Nzoia', 'Trans Nzoia'), ('Migori', 'Migori'), ('Samburu', 'Samburu'), ('Nyeri', 'Nyeri'), ('Nairobi', 'Nairobi'), ('Taita-Taveta', 'Taita-Taveta'), ('Makueni', 'Makueni'), ('Nyamira', 'Nyamira'), ('Embu', 'Embu'), ('Mombasa', 'Mombasa'), ('Machakos', 'Machakos'), ('Kwale', 'Kwale'), ('Tana River', 'Tana River'), ('Nakuru', 'Nakuru'), ('Nandi', 'Nandi'), ('Lamu', 'Lamu'), ('Kakamega', 'Kakamega'), ("Murang'a", 'Murang'), ('Turkana', 'Turkana'), ('Busia', 'Busia'), ('Kajiado', 'Kajiado'), ('Wajir', 'Wajir'), ('West Pokot', 'West Pokot'), ('Kitui', 'Kitui'), ('Kisumu', 'Kisumu'), ('Homa Bay', 'Homa Bay'), ('Nyandarua', 'Nyandarua'), ('Kilifi', 'Kilifi'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Garissa', 'Garissa'), ('Uasin Gishu', 'Uasin Gishu'), ('Kirinyaga', 'Kirinyaga'), ('Bungoma', 'Bungoma'), ('Baringo', 'Baringo'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Marsabit', 'Marsabit'), ('Laikipia', 'Laikipia'), ('Mandera', 'Mandera'), ('Narok', 'Narok'), ('Kericho', 'Kericho'), ('Isiolo', 'Homa Bay'), ('Kisii', 'Kisii')], max_length=15),
        ),
        migrations.AlterField(
            model_name='volunteerregistration',
            name='location',
            field=models.CharField(choices=[('Vihiga', 'Vihiga'), ('Bomet', 'Bomet'), ('Kiambu', 'Kiambu'), ('Siaya', 'Siaya'), ('Meru', 'Meru'), ('Trans Nzoia', 'Trans Nzoia'), ('Migori', 'Migori'), ('Samburu', 'Samburu'), ('Nyeri', 'Nyeri'), ('Nairobi', 'Nairobi'), ('Taita-Taveta', 'Taita-Taveta'), ('Makueni', 'Makueni'), ('Nyamira', 'Nyamira'), ('Embu', 'Embu'), ('Mombasa', 'Mombasa'), ('Machakos', 'Machakos'), ('Kwale', 'Kwale'), ('Tana River', 'Tana River'), ('Nakuru', 'Nakuru'), ('Nandi', 'Nandi'), ('Lamu', 'Lamu'), ('Kakamega', 'Kakamega'), ("Murang'a", 'Murang'), ('Turkana', 'Turkana'), ('Busia', 'Busia'), ('Kajiado', 'Kajiado'), ('Wajir', 'Wajir'), ('West Pokot', 'West Pokot'), ('Kitui', 'Kitui'), ('Kisumu', 'Kisumu'), ('Homa Bay', 'Homa Bay'), ('Nyandarua', 'Nyandarua'), ('Kilifi', 'Kilifi'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Garissa', 'Garissa'), ('Uasin Gishu', 'Uasin Gishu'), ('Kirinyaga', 'Kirinyaga'), ('Bungoma', 'Bungoma'), ('Baringo', 'Baringo'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Marsabit', 'Marsabit'), ('Laikipia', 'Laikipia'), ('Mandera', 'Mandera'), ('Narok', 'Narok'), ('Kericho', 'Kericho'), ('Isiolo', 'Homa Bay'), ('Kisii', 'Kisii')], max_length=100),
        ),
        migrations.AlterField(
            model_name='volunteerregistration',
            name='volunteer_id',
            field=models.CharField(default=uuid.UUID('103a0e4b-58de-4cab-8c17-5048964b821f'), max_length=20, primary_key=True, serialize=False),
        ),
    ]