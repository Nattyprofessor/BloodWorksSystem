# Generated by Django 3.0.5 on 2023-07-15 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0010_auto_20230714_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostedblooddrives',
            name='county',
            field=models.CharField(choices=[('West Pokot', 'West Pokot'), ('Kirinyaga', 'Kirinyaga'), ('Marsabit', 'Marsabit'), ('Kakamega', 'Kakamega'), ('Tana River', 'Tana River'), ('Busia', 'Busia'), ('Machakos', 'Machakos'), ('Narok', 'Narok'), ('Samburu', 'Samburu'), ('Nyamira', 'Nyamira'), ('Makueni', 'Makueni'), ('Uasin Gishu', 'Uasin Gishu'), ('Nakuru', 'Nakuru'), ('Kwale', 'Kwale'), ('Turkana', 'Turkana'), ('Kiambu', 'Kiambu'), ('Nandi', 'Nandi'), ('Taita-Taveta', 'Taita-Taveta'), ('Nairobi', 'Nairobi'), ('Baringo', 'Baringo'), ('Vihiga', 'Vihiga'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Meru', 'Meru'), ('Bungoma', 'Bungoma'), ("Murang'a", 'Murang'), ('Wajir', 'Wajir'), ('Bomet', 'Bomet'), ('Garissa', 'Garissa'), ('Embu', 'Embu'), ('Homa Bay', 'Homa Bay'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Trans Nzoia', 'Trans Nzoia'), ('Nyandarua', 'Nyandarua'), ('Siaya', 'Siaya'), ('Kisii', 'Kisii'), ('Mandera', 'Mandera'), ('Mombasa', 'Mombasa'), ('Nyeri', 'Nyeri'), ('Kilifi', 'Kilifi'), ('Kitui', 'Kitui'), ('Kajiado', 'Kajiado'), ('Laikipia', 'Laikipia'), ('Isiolo', 'Homa Bay'), ('Kisumu', 'Kisumu'), ('Lamu', 'Lamu'), ('Kericho', 'Kericho'), ('Migori', 'Migori')], max_length=15),
        ),
        migrations.AlterField(
            model_name='volunteerregistration',
            name='location',
            field=models.CharField(choices=[('West Pokot', 'West Pokot'), ('Kirinyaga', 'Kirinyaga'), ('Marsabit', 'Marsabit'), ('Kakamega', 'Kakamega'), ('Tana River', 'Tana River'), ('Busia', 'Busia'), ('Machakos', 'Machakos'), ('Narok', 'Narok'), ('Samburu', 'Samburu'), ('Nyamira', 'Nyamira'), ('Makueni', 'Makueni'), ('Uasin Gishu', 'Uasin Gishu'), ('Nakuru', 'Nakuru'), ('Kwale', 'Kwale'), ('Turkana', 'Turkana'), ('Kiambu', 'Kiambu'), ('Nandi', 'Nandi'), ('Taita-Taveta', 'Taita-Taveta'), ('Nairobi', 'Nairobi'), ('Baringo', 'Baringo'), ('Vihiga', 'Vihiga'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Meru', 'Meru'), ('Bungoma', 'Bungoma'), ("Murang'a", 'Murang'), ('Wajir', 'Wajir'), ('Bomet', 'Bomet'), ('Garissa', 'Garissa'), ('Embu', 'Embu'), ('Homa Bay', 'Homa Bay'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Trans Nzoia', 'Trans Nzoia'), ('Nyandarua', 'Nyandarua'), ('Siaya', 'Siaya'), ('Kisii', 'Kisii'), ('Mandera', 'Mandera'), ('Mombasa', 'Mombasa'), ('Nyeri', 'Nyeri'), ('Kilifi', 'Kilifi'), ('Kitui', 'Kitui'), ('Kajiado', 'Kajiado'), ('Laikipia', 'Laikipia'), ('Isiolo', 'Homa Bay'), ('Kisumu', 'Kisumu'), ('Lamu', 'Lamu'), ('Kericho', 'Kericho'), ('Migori', 'Migori')], max_length=100),
        ),
    ]
