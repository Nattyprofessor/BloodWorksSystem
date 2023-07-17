# Generated by Django 4.2.3 on 2023-07-17 08:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0026_alter_blooddrives_county_alter_blooddrives_drive_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddrives',
            name='county',
            field=models.CharField(choices=[('Uasin Gishu', 'Uasin Gishu'), ('Busia', 'Busia'), ('Taita-Taveta', 'Taita-Taveta'), ('Nandi', 'Nandi'), ('Homa Bay', 'Homa Bay'), ('Isiolo', 'Homa Bay'), ('Laikipia', 'Laikipia'), ('Makueni', 'Makueni'), ('Embu', 'Embu'), ('Samburu', 'Samburu'), ('Nyeri', 'Nyeri'), ('Kisumu', 'Kisumu'), ('Turkana', 'Turkana'), ('Nyandarua', 'Nyandarua'), ('Kitui', 'Kitui'), ('West Pokot', 'West Pokot'), ('Garissa', 'Garissa'), ('Bungoma', 'Bungoma'), ('Kwale', 'Kwale'), ('Baringo', 'Baringo'), ('Kisii', 'Kisii'), ('Nairobi', 'Nairobi'), ('Narok', 'Narok'), ('Kakamega', 'Kakamega'), ('Migori', 'Migori'), ('Nakuru', 'Nakuru'), ('Kilifi', 'Kilifi'), ('Machakos', 'Machakos'), ('Meru', 'Meru'), ('Siaya', 'Siaya'), ('Mandera', 'Mandera'), ('Vihiga', 'Vihiga'), ('Kirinyaga', 'Kirinyaga'), ('Tana River', 'Tana River'), ('Kajiado', 'Kajiado'), ('Lamu', 'Lamu'), ('Nyamira', 'Nyamira'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ("Murang'a", 'Murang'), ('Marsabit', 'Marsabit'), ('Bomet', 'Bomet'), ('Kericho', 'Kericho'), ('Kiambu', 'Kiambu'), ('Mombasa', 'Mombasa'), ('Trans Nzoia', 'Trans Nzoia'), ('Wajir', 'Wajir'), ('Tharaka-Nithi', 'Tharaka-Nithi')], max_length=15),
        ),
        migrations.AlterField(
            model_name='blooddrives',
            name='drive_id',
            field=models.CharField(default=uuid.UUID('1b626e98-4425-4146-a951-bbabfa2ade55'), max_length=20, primary_key=True, serialize=False),
        ),
    ]