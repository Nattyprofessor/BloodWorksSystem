# Generated by Django 3.0.5 on 2023-07-15 16:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0021_auto_20230715_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostedblooddrives',
            name='county',
            field=models.CharField(choices=[('Turkana', 'Turkana'), ('Migori', 'Migori'), ('Bomet', 'Bomet'), ('Kericho', 'Kericho'), ('Kilifi', 'Kilifi'), ('Kitui', 'Kitui'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Narok', 'Narok'), ('Kiambu', 'Kiambu'), ('Tana River', 'Tana River'), ('Kajiado', 'Kajiado'), ('Isiolo', 'Homa Bay'), ('Laikipia', 'Laikipia'), ('Nakuru', 'Nakuru'), ('Siaya', 'Siaya'), ('Embu', 'Embu'), ('Bungoma', 'Bungoma'), ('Nandi', 'Nandi'), ('Taita-Taveta', 'Taita-Taveta'), ('Machakos', 'Machakos'), ('Kisii', 'Kisii'), ('Garissa', 'Garissa'), ('Kisumu', 'Kisumu'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Busia', 'Busia'), ('Homa Bay', 'Homa Bay'), ('Wajir', 'Wajir'), ('Kakamega', 'Kakamega'), ('Makueni', 'Makueni'), ('Baringo', 'Baringo'), ('West Pokot', 'West Pokot'), ('Vihiga', 'Vihiga'), ('Nairobi', 'Nairobi'), ('Nyandarua', 'Nyandarua'), ('Nyamira', 'Nyamira'), ('Mombasa', 'Mombasa'), ("Murang'a", 'Murang'), ('Kwale', 'Kwale'), ('Marsabit', 'Marsabit'), ('Mandera', 'Mandera'), ('Lamu', 'Lamu'), ('Kirinyaga', 'Kirinyaga'), ('Uasin Gishu', 'Uasin Gishu'), ('Trans Nzoia', 'Trans Nzoia'), ('Nyeri', 'Nyeri'), ('Samburu', 'Samburu'), ('Meru', 'Meru')], max_length=15),
        ),
        migrations.AlterField(
            model_name='volunteerregistration',
            name='location',
            field=models.CharField(choices=[('Turkana', 'Turkana'), ('Migori', 'Migori'), ('Bomet', 'Bomet'), ('Kericho', 'Kericho'), ('Kilifi', 'Kilifi'), ('Kitui', 'Kitui'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Narok', 'Narok'), ('Kiambu', 'Kiambu'), ('Tana River', 'Tana River'), ('Kajiado', 'Kajiado'), ('Isiolo', 'Homa Bay'), ('Laikipia', 'Laikipia'), ('Nakuru', 'Nakuru'), ('Siaya', 'Siaya'), ('Embu', 'Embu'), ('Bungoma', 'Bungoma'), ('Nandi', 'Nandi'), ('Taita-Taveta', 'Taita-Taveta'), ('Machakos', 'Machakos'), ('Kisii', 'Kisii'), ('Garissa', 'Garissa'), ('Kisumu', 'Kisumu'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Busia', 'Busia'), ('Homa Bay', 'Homa Bay'), ('Wajir', 'Wajir'), ('Kakamega', 'Kakamega'), ('Makueni', 'Makueni'), ('Baringo', 'Baringo'), ('West Pokot', 'West Pokot'), ('Vihiga', 'Vihiga'), ('Nairobi', 'Nairobi'), ('Nyandarua', 'Nyandarua'), ('Nyamira', 'Nyamira'), ('Mombasa', 'Mombasa'), ("Murang'a", 'Murang'), ('Kwale', 'Kwale'), ('Marsabit', 'Marsabit'), ('Mandera', 'Mandera'), ('Lamu', 'Lamu'), ('Kirinyaga', 'Kirinyaga'), ('Uasin Gishu', 'Uasin Gishu'), ('Trans Nzoia', 'Trans Nzoia'), ('Nyeri', 'Nyeri'), ('Samburu', 'Samburu'), ('Meru', 'Meru')], max_length=100),
        ),
        migrations.AlterField(
            model_name='volunteerregistration',
            name='volunteer_id',
            field=models.CharField(default=uuid.UUID('7638f0c7-5432-4269-aa44-f4e2f8786894'), max_length=20, primary_key=True, serialize=False),
        ),
    ]
