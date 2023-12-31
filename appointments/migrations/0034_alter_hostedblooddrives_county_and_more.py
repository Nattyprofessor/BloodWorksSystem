# Generated by Django 4.2.3 on 2023-07-17 17:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0033_alter_hostedblooddrives_county_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostedblooddrives',
            name='county',
            field=models.CharField(choices=[('Kakamega', 'Kakamega'), ('Kwale', 'Kwale'), ('Tana River', 'Tana River'), ('Kilifi', 'Kilifi'), ('Mombasa', 'Mombasa'), ('Embu', 'Embu'), ('Taita-Taveta', 'Taita-Taveta'), ('Mandera', 'Mandera'), ('West Pokot', 'West Pokot'), ('Nyandarua', 'Nyandarua'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Bomet', 'Bomet'), ('Trans Nzoia', 'Trans Nzoia'), ('Siaya', 'Siaya'), ('Nandi', 'Nandi'), ("Murang'a", 'Murang'), ('Samburu', 'Samburu'), ('Wajir', 'Wajir'), ('Meru', 'Meru'), ('Lamu', 'Lamu'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Homa Bay', 'Homa Bay'), ('Nakuru', 'Nakuru'), ('Kisumu', 'Kisumu'), ('Bungoma', 'Bungoma'), ('Nairobi', 'Nairobi'), ('Garissa', 'Garissa'), ('Makueni', 'Makueni'), ('Kitui', 'Kitui'), ('Migori', 'Migori'), ('Nyeri', 'Nyeri'), ('Kericho', 'Kericho'), ('Uasin Gishu', 'Uasin Gishu'), ('Laikipia', 'Laikipia'), ('Vihiga', 'Vihiga'), ('Machakos', 'Machakos'), ('Baringo', 'Baringo'), ('Turkana', 'Turkana'), ('Marsabit', 'Marsabit'), ('Kisii', 'Kisii'), ('Kirinyaga', 'Kirinyaga'), ('Narok', 'Narok'), ('Isiolo', 'Homa Bay'), ('Nyamira', 'Nyamira'), ('Busia', 'Busia'), ('Kiambu', 'Kiambu'), ('Kajiado', 'Kajiado')], max_length=15),
        ),
        migrations.AlterField(
            model_name='volunteerregistration',
            name='location',
            field=models.CharField(choices=[('Kakamega', 'Kakamega'), ('Kwale', 'Kwale'), ('Tana River', 'Tana River'), ('Kilifi', 'Kilifi'), ('Mombasa', 'Mombasa'), ('Embu', 'Embu'), ('Taita-Taveta', 'Taita-Taveta'), ('Mandera', 'Mandera'), ('West Pokot', 'West Pokot'), ('Nyandarua', 'Nyandarua'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Bomet', 'Bomet'), ('Trans Nzoia', 'Trans Nzoia'), ('Siaya', 'Siaya'), ('Nandi', 'Nandi'), ("Murang'a", 'Murang'), ('Samburu', 'Samburu'), ('Wajir', 'Wajir'), ('Meru', 'Meru'), ('Lamu', 'Lamu'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Homa Bay', 'Homa Bay'), ('Nakuru', 'Nakuru'), ('Kisumu', 'Kisumu'), ('Bungoma', 'Bungoma'), ('Nairobi', 'Nairobi'), ('Garissa', 'Garissa'), ('Makueni', 'Makueni'), ('Kitui', 'Kitui'), ('Migori', 'Migori'), ('Nyeri', 'Nyeri'), ('Kericho', 'Kericho'), ('Uasin Gishu', 'Uasin Gishu'), ('Laikipia', 'Laikipia'), ('Vihiga', 'Vihiga'), ('Machakos', 'Machakos'), ('Baringo', 'Baringo'), ('Turkana', 'Turkana'), ('Marsabit', 'Marsabit'), ('Kisii', 'Kisii'), ('Kirinyaga', 'Kirinyaga'), ('Narok', 'Narok'), ('Isiolo', 'Homa Bay'), ('Nyamira', 'Nyamira'), ('Busia', 'Busia'), ('Kiambu', 'Kiambu'), ('Kajiado', 'Kajiado')], max_length=100),
        ),
        migrations.AlterField(
            model_name='volunteerregistration',
            name='volunteer_id',
            field=models.CharField(default=uuid.UUID('52544c0d-f381-46b2-83e9-92ad8f631b92'), max_length=20, primary_key=True, serialize=False),
        ),
    ]
