# Generated by Django 3.0.5 on 2023-07-14 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0008_auto_20230713_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddrives',
            name='county',
            field=models.CharField(choices=[('Bungoma', 'Bungoma'), ('Nyeri', 'Nyeri'), ('Kajiado', 'Kajiado'), ('Baringo', 'Baringo'), ('Busia', 'Busia'), ('Tana River', 'Tana River'), ('Mombasa', 'Mombasa'), ('Kisii', 'Kisii'), ('Garissa', 'Garissa'), ('Kericho', 'Kericho'), ('Mandera', 'Mandera'), ('Kisumu', 'Kisumu'), ('Kwale', 'Kwale'), ('Siaya', 'Siaya'), ('Marsabit', 'Marsabit'), ("Murang'a", 'Murang'), ('Nyandarua', 'Nyandarua'), ('Uasin Gishu', 'Uasin Gishu'), ('Kiambu', 'Kiambu'), ('Turkana', 'Turkana'), ('Bomet', 'Bomet'), ('Taita-Taveta', 'Taita-Taveta'), ('Migori', 'Migori'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Machakos', 'Machakos'), ('Kirinyaga', 'Kirinyaga'), ('Kakamega', 'Kakamega'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Kitui', 'Kitui'), ('Kilifi', 'Kilifi'), ('Samburu', 'Samburu'), ('Laikipia', 'Laikipia'), ('Nakuru', 'Nakuru'), ('Meru', 'Meru'), ('Nyamira', 'Nyamira'), ('Trans Nzoia', 'Trans Nzoia'), ('Nandi', 'Nandi'), ('Makueni', 'Makueni'), ('West Pokot', 'West Pokot'), ('Wajir', 'Wajir'), ('Embu', 'Embu'), ('Lamu', 'Lamu'), ('Isiolo', 'Homa Bay'), ('Vihiga', 'Vihiga'), ('Homa Bay', 'Homa Bay'), ('Narok', 'Narok'), ('Nairobi', 'Nairobi')], max_length=15),
        ),
    ]
