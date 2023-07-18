# Generated by Django 4.2.3 on 2023-07-18 11:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0035_alter_blooddrives_county_alter_blooddrives_drive_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddrives',
            name='county',
            field=models.CharField(choices=[('Kajiado', 'Kajiado'), ('Baringo', 'Baringo'), ('Nyamira', 'Nyamira'), ('Wajir', 'Wajir'), ('Kwale', 'Kwale'), ('Garissa', 'Garissa'), ("Murang'a", 'Murang'), ('Taita-Taveta', 'Taita-Taveta'), ('Siaya', 'Siaya'), ('Vihiga', 'Vihiga'), ('West Pokot', 'West Pokot'), ('Turkana', 'Turkana'), ('Nairobi', 'Nairobi'), ('Machakos', 'Machakos'), ('Kitui', 'Kitui'), ('Busia', 'Busia'), ('Kiambu', 'Kiambu'), ('Laikipia', 'Laikipia'), ('Marsabit', 'Marsabit'), ('Embu', 'Embu'), ('Bungoma', 'Bungoma'), ('Tana River', 'Tana River'), ('Isiolo', 'Homa Bay'), ('Kericho', 'Kericho'), ('Nyandarua', 'Nyandarua'), ('Kakamega', 'Kakamega'), ('Mombasa', 'Mombasa'), ('Uasin Gishu', 'Uasin Gishu'), ('Samburu', 'Samburu'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Nandi', 'Nandi'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Narok', 'Narok'), ('Migori', 'Migori'), ('Trans Nzoia', 'Trans Nzoia'), ('Kilifi', 'Kilifi'), ('Homa Bay', 'Homa Bay'), ('Bomet', 'Bomet'), ('Nyeri', 'Nyeri'), ('Nakuru', 'Nakuru'), ('Kisumu', 'Kisumu'), ('Kirinyaga', 'Kirinyaga'), ('Kisii', 'Kisii'), ('Meru', 'Meru'), ('Mandera', 'Mandera'), ('Makueni', 'Makueni'), ('Lamu', 'Lamu')], max_length=15),
        ),
        migrations.AlterField(
            model_name='blooddrives',
            name='drive_id',
            field=models.CharField(default=uuid.UUID('aeef0c5d-9c8b-4d1e-b611-cdee853de755'), max_length=20, primary_key=True, serialize=False),
        ),
    ]
