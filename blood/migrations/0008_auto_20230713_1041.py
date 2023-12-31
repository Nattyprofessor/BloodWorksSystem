# Generated by Django 3.0.5 on 2023-07-13 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0007_auto_20230713_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddrives',
            name='county',
            field=models.CharField(choices=[('Narok', 'Narok'), ('Mombasa', 'Mombasa'), ('Wajir', 'Wajir'), ('Isiolo', 'Homa Bay'), ('Nakuru', 'Nakuru'), ('Bungoma', 'Bungoma'), ('Samburu', 'Samburu'), ('Garissa', 'Garissa'), ('Kisii', 'Kisii'), ('Kiambu', 'Kiambu'), ('Bomet', 'Bomet'), ('Migori', 'Migori'), ('Vihiga', 'Vihiga'), ('West Pokot', 'West Pokot'), ('Kilifi', 'Kilifi'), ('Laikipia', 'Laikipia'), ('Baringo', 'Baringo'), ('Trans Nzoia', 'Trans Nzoia'), ('Kitui', 'Kitui'), ('Lamu', 'Lamu'), ('Nyandarua', 'Nyandarua'), ('Meru', 'Meru'), ('Kajiado', 'Kajiado'), ('Nairobi', 'Nairobi'), ('Makueni', 'Makueni'), ('Homa Bay', 'Homa Bay'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Turkana', 'Turkana'), ('Nyamira', 'Nyamira'), ('Taita-Taveta', 'Taita-Taveta'), ('Kirinyaga', 'Kirinyaga'), ('Mandera', 'Mandera'), ("Murang'a", 'Murang'), ('Embu', 'Embu'), ('Uasin Gishu', 'Uasin Gishu'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Nyeri', 'Nyeri'), ('Kisumu', 'Kisumu'), ('Kericho', 'Kericho'), ('Kakamega', 'Kakamega'), ('Siaya', 'Siaya'), ('Busia', 'Busia'), ('Tana River', 'Tana River'), ('Nandi', 'Nandi'), ('Machakos', 'Machakos'), ('Marsabit', 'Marsabit'), ('Kwale', 'Kwale')], max_length=15),
        ),
    ]
