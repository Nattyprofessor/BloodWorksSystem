# Generated by Django 3.0.5 on 2023-07-15 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0013_auto_20230715_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostedblooddrives',
            name='county',
            field=models.CharField(choices=[('Siaya', 'Siaya'), ('Nairobi', 'Nairobi'), ('Narok', 'Narok'), ('Migori', 'Migori'), ('Machakos', 'Machakos'), ('Busia', 'Busia'), ('Wajir', 'Wajir'), ('Vihiga', 'Vihiga'), ('Bungoma', 'Bungoma'), ('Mombasa', 'Mombasa'), ('Samburu', 'Samburu'), ('Bomet', 'Bomet'), ('Kakamega', 'Kakamega'), ('Lamu', 'Lamu'), ('Mandera', 'Mandera'), ('Uasin Gishu', 'Uasin Gishu'), ('Trans Nzoia', 'Trans Nzoia'), ('Makueni', 'Makueni'), ('Kisumu', 'Kisumu'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Kajiado', 'Kajiado'), ('Marsabit', 'Marsabit'), ('Nyandarua', 'Nyandarua'), ('Nakuru', 'Nakuru'), ('Kirinyaga', 'Kirinyaga'), ('Embu', 'Embu'), ('Taita-Taveta', 'Taita-Taveta'), ('Isiolo', 'Homa Bay'), ('Kisii', 'Kisii'), ('Garissa', 'Garissa'), ('Laikipia', 'Laikipia'), ('Kwale', 'Kwale'), ("Murang'a", 'Murang'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Nandi', 'Nandi'), ('Nyamira', 'Nyamira'), ('Baringo', 'Baringo'), ('Tana River', 'Tana River'), ('Turkana', 'Turkana'), ('Kitui', 'Kitui'), ('Kericho', 'Kericho'), ('Homa Bay', 'Homa Bay'), ('Kiambu', 'Kiambu'), ('Nyeri', 'Nyeri'), ('West Pokot', 'West Pokot'), ('Meru', 'Meru'), ('Kilifi', 'Kilifi')], max_length=15),
        ),
        migrations.AlterField(
            model_name='volunteerregistration',
            name='location',
            field=models.CharField(choices=[('Siaya', 'Siaya'), ('Nairobi', 'Nairobi'), ('Narok', 'Narok'), ('Migori', 'Migori'), ('Machakos', 'Machakos'), ('Busia', 'Busia'), ('Wajir', 'Wajir'), ('Vihiga', 'Vihiga'), ('Bungoma', 'Bungoma'), ('Mombasa', 'Mombasa'), ('Samburu', 'Samburu'), ('Bomet', 'Bomet'), ('Kakamega', 'Kakamega'), ('Lamu', 'Lamu'), ('Mandera', 'Mandera'), ('Uasin Gishu', 'Uasin Gishu'), ('Trans Nzoia', 'Trans Nzoia'), ('Makueni', 'Makueni'), ('Kisumu', 'Kisumu'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Kajiado', 'Kajiado'), ('Marsabit', 'Marsabit'), ('Nyandarua', 'Nyandarua'), ('Nakuru', 'Nakuru'), ('Kirinyaga', 'Kirinyaga'), ('Embu', 'Embu'), ('Taita-Taveta', 'Taita-Taveta'), ('Isiolo', 'Homa Bay'), ('Kisii', 'Kisii'), ('Garissa', 'Garissa'), ('Laikipia', 'Laikipia'), ('Kwale', 'Kwale'), ("Murang'a", 'Murang'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Nandi', 'Nandi'), ('Nyamira', 'Nyamira'), ('Baringo', 'Baringo'), ('Tana River', 'Tana River'), ('Turkana', 'Turkana'), ('Kitui', 'Kitui'), ('Kericho', 'Kericho'), ('Homa Bay', 'Homa Bay'), ('Kiambu', 'Kiambu'), ('Nyeri', 'Nyeri'), ('West Pokot', 'West Pokot'), ('Meru', 'Meru'), ('Kilifi', 'Kilifi')], max_length=100),
        ),
    ]
