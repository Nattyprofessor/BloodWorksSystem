# Generated by Django 4.2.3 on 2023-07-23 15:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0039_alter_hostedblooddrives_county_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostedblooddrives',
            name='county',
            field=models.CharField(choices=[('Meru', 'Meru'), ('Mombasa', 'Mombasa'), ('Tana River', 'Tana River'), ('Lamu', 'Lamu'), ('Marsabit', 'Marsabit'), ('Uasin Gishu', 'Uasin Gishu'), ('Embu', 'Embu'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Siaya', 'Siaya'), ('Kajiado', 'Kajiado'), ("Murang'a", 'Murang'), ('Kitui', 'Kitui'), ('West Pokot', 'West Pokot'), ('Isiolo', 'Homa Bay'), ('Taita-Taveta', 'Taita-Taveta'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Kwale', 'Kwale'), ('Kisumu', 'Kisumu'), ('Nyeri', 'Nyeri'), ('Machakos', 'Machakos'), ('Migori', 'Migori'), ('Garissa', 'Garissa'), ('Baringo', 'Baringo'), ('Kisii', 'Kisii'), ('Nairobi', 'Nairobi'), ('Turkana', 'Turkana'), ('Nyamira', 'Nyamira'), ('Trans Nzoia', 'Trans Nzoia'), ('Kericho', 'Kericho'), ('Nyandarua', 'Nyandarua'), ('Homa Bay', 'Homa Bay'), ('Busia', 'Busia'), ('Nakuru', 'Nakuru'), ('Kirinyaga', 'Kirinyaga'), ('Wajir', 'Wajir'), ('Nandi', 'Nandi'), ('Mandera', 'Mandera'), ('Laikipia', 'Laikipia'), ('Kakamega', 'Kakamega'), ('Narok', 'Narok'), ('Vihiga', 'Vihiga'), ('Kilifi', 'Kilifi'), ('Makueni', 'Makueni'), ('Bungoma', 'Bungoma'), ('Samburu', 'Samburu'), ('Kiambu', 'Kiambu'), ('Bomet', 'Bomet')], max_length=15),
        ),
        migrations.AlterField(
            model_name='volunteerregistration',
            name='location',
            field=models.CharField(choices=[('Meru', 'Meru'), ('Mombasa', 'Mombasa'), ('Tana River', 'Tana River'), ('Lamu', 'Lamu'), ('Marsabit', 'Marsabit'), ('Uasin Gishu', 'Uasin Gishu'), ('Embu', 'Embu'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Siaya', 'Siaya'), ('Kajiado', 'Kajiado'), ("Murang'a", 'Murang'), ('Kitui', 'Kitui'), ('West Pokot', 'West Pokot'), ('Isiolo', 'Homa Bay'), ('Taita-Taveta', 'Taita-Taveta'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Kwale', 'Kwale'), ('Kisumu', 'Kisumu'), ('Nyeri', 'Nyeri'), ('Machakos', 'Machakos'), ('Migori', 'Migori'), ('Garissa', 'Garissa'), ('Baringo', 'Baringo'), ('Kisii', 'Kisii'), ('Nairobi', 'Nairobi'), ('Turkana', 'Turkana'), ('Nyamira', 'Nyamira'), ('Trans Nzoia', 'Trans Nzoia'), ('Kericho', 'Kericho'), ('Nyandarua', 'Nyandarua'), ('Homa Bay', 'Homa Bay'), ('Busia', 'Busia'), ('Nakuru', 'Nakuru'), ('Kirinyaga', 'Kirinyaga'), ('Wajir', 'Wajir'), ('Nandi', 'Nandi'), ('Mandera', 'Mandera'), ('Laikipia', 'Laikipia'), ('Kakamega', 'Kakamega'), ('Narok', 'Narok'), ('Vihiga', 'Vihiga'), ('Kilifi', 'Kilifi'), ('Makueni', 'Makueni'), ('Bungoma', 'Bungoma'), ('Samburu', 'Samburu'), ('Kiambu', 'Kiambu'), ('Bomet', 'Bomet')], max_length=100),
        ),
        migrations.AlterField(
            model_name='volunteerregistration',
            name='volunteer_id',
            field=models.CharField(default=uuid.UUID('dc7d07ad-5a5a-4a9b-8652-2ad3e2af93aa'), max_length=20, primary_key=True, serialize=False),
        ),
    ]
