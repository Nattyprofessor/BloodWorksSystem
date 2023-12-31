# Generated by Django 4.2.3 on 2023-07-18 11:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0037_alter_hostedblooddrives_county_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostedblooddrives',
            name='county',
            field=models.CharField(choices=[('Kajiado', 'Kajiado'), ('Baringo', 'Baringo'), ('Nyamira', 'Nyamira'), ('Wajir', 'Wajir'), ('Kirinyaga', 'Kirinyaga'), ('Kwale', 'Kwale'), ('Garissa', 'Garissa'), ("Murang'a", 'Murang'), ('Taita-Taveta', 'Taita-Taveta'), ('Siaya', 'Siaya'), ('Vihiga', 'Vihiga'), ('West Pokot', 'West Pokot'), ('Turkana', 'Turkana'), ('Nairobi', 'Nairobi'), ('Machakos', 'Machakos'), ('Kitui', 'Kitui'), ('Busia', 'Busia'), ('Kiambu', 'Kiambu'), ('Marsabit', 'Marsabit'), ('Laikipia', 'Laikipia'), ('Bungoma', 'Bungoma'), ('Tana River', 'Tana River'), ('Isiolo', 'Homa Bay'), ('Kericho', 'Kericho'), ('Nyandarua', 'Nyandarua'), ('Kakamega', 'Kakamega'), ('Mombasa', 'Mombasa'), ('Uasin Gishu', 'Uasin Gishu'), ('Samburu', 'Samburu'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Nandi', 'Nandi'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Narok', 'Narok'), ('Migori', 'Migori'), ('Trans Nzoia', 'Trans Nzoia'), ('Kilifi', 'Kilifi'), ('Homa Bay', 'Homa Bay'), ('Bomet', 'Bomet'), ('Nyeri', 'Nyeri'), ('Nakuru', 'Nakuru'), ('Kisumu', 'Kisumu'), ('Embu', 'Embu'), ('Kisii', 'Kisii'), ('Meru', 'Meru'), ('Mandera', 'Mandera'), ('Makueni', 'Makueni'), ('Lamu', 'Lamu')], max_length=15),
        ),
        migrations.AlterField(
            model_name='volunteerregistration',
            name='location',
            field=models.CharField(choices=[('Kajiado', 'Kajiado'), ('Baringo', 'Baringo'), ('Nyamira', 'Nyamira'), ('Wajir', 'Wajir'), ('Kirinyaga', 'Kirinyaga'), ('Kwale', 'Kwale'), ('Garissa', 'Garissa'), ("Murang'a", 'Murang'), ('Taita-Taveta', 'Taita-Taveta'), ('Siaya', 'Siaya'), ('Vihiga', 'Vihiga'), ('West Pokot', 'West Pokot'), ('Turkana', 'Turkana'), ('Nairobi', 'Nairobi'), ('Machakos', 'Machakos'), ('Kitui', 'Kitui'), ('Busia', 'Busia'), ('Kiambu', 'Kiambu'), ('Marsabit', 'Marsabit'), ('Laikipia', 'Laikipia'), ('Bungoma', 'Bungoma'), ('Tana River', 'Tana River'), ('Isiolo', 'Homa Bay'), ('Kericho', 'Kericho'), ('Nyandarua', 'Nyandarua'), ('Kakamega', 'Kakamega'), ('Mombasa', 'Mombasa'), ('Uasin Gishu', 'Uasin Gishu'), ('Samburu', 'Samburu'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Nandi', 'Nandi'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Narok', 'Narok'), ('Migori', 'Migori'), ('Trans Nzoia', 'Trans Nzoia'), ('Kilifi', 'Kilifi'), ('Homa Bay', 'Homa Bay'), ('Bomet', 'Bomet'), ('Nyeri', 'Nyeri'), ('Nakuru', 'Nakuru'), ('Kisumu', 'Kisumu'), ('Embu', 'Embu'), ('Kisii', 'Kisii'), ('Meru', 'Meru'), ('Mandera', 'Mandera'), ('Makueni', 'Makueni'), ('Lamu', 'Lamu')], max_length=100),
        ),
        migrations.AlterField(
            model_name='volunteerregistration',
            name='volunteer_id',
            field=models.CharField(default=uuid.UUID('cf46db33-68e6-4291-927c-5176c79e979f'), max_length=20, primary_key=True, serialize=False),
        ),
    ]
