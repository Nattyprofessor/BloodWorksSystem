# Generated by Django 4.2.3 on 2023-07-17 20:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0033_alter_blooddrives_county_alter_blooddrives_drive_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddrives',
            name='county',
            field=models.CharField(choices=[('Garissa', 'Garissa'), ('Bomet', 'Bomet'), ('Baringo', 'Baringo'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Bungoma', 'Bungoma'), ('Makueni', 'Makueni'), ("Murang'a", 'Murang'), ('Nakuru', 'Nakuru'), ('Nyamira', 'Nyamira'), ('Uasin Gishu', 'Uasin Gishu'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Laikipia', 'Laikipia'), ('Migori', 'Migori'), ('Turkana', 'Turkana'), ('Nyandarua', 'Nyandarua'), ('Meru', 'Meru'), ('Siaya', 'Siaya'), ('Lamu', 'Lamu'), ('Taita-Taveta', 'Taita-Taveta'), ('Kilifi', 'Kilifi'), ('Vihiga', 'Vihiga'), ('Kitui', 'Kitui'), ('Kakamega', 'Kakamega'), ('Kajiado', 'Kajiado'), ('Tana River', 'Tana River'), ('Nairobi', 'Nairobi'), ('West Pokot', 'West Pokot'), ('Busia', 'Busia'), ('Kisumu', 'Kisumu'), ('Wajir', 'Wajir'), ('Narok', 'Narok'), ('Marsabit', 'Marsabit'), ('Nandi', 'Nandi'), ('Homa Bay', 'Homa Bay'), ('Nyeri', 'Nyeri'), ('Samburu', 'Samburu'), ('Mombasa', 'Mombasa'), ('Kirinyaga', 'Kirinyaga'), ('Mandera', 'Mandera'), ('Embu', 'Embu'), ('Machakos', 'Machakos'), ('Kiambu', 'Kiambu'), ('Isiolo', 'Homa Bay'), ('Kwale', 'Kwale'), ('Kisii', 'Kisii'), ('Kericho', 'Kericho'), ('Trans Nzoia', 'Trans Nzoia')], max_length=15),
        ),
        migrations.AlterField(
            model_name='blooddrives',
            name='drive_id',
            field=models.CharField(default=uuid.UUID('86dbc336-d045-4efa-9f2d-371ffd793d79'), max_length=20, primary_key=True, serialize=False),
        ),
    ]
