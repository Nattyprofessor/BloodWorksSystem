# Generated by Django 3.0.5 on 2023-07-15 22:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0022_auto_20230715_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddrives',
            name='county',
            field=models.CharField(choices=[('Narok', 'Narok'), ('Marsabit', 'Marsabit'), ('Kitui', 'Kitui'), ('Kirinyaga', 'Kirinyaga'), ('Kiambu', 'Kiambu'), ('Nyamira', 'Nyamira'), ('Bungoma', 'Bungoma'), ('Kisumu', 'Kisumu'), ('Kisii', 'Kisii'), ('Homa Bay', 'Homa Bay'), ('Nyandarua', 'Nyandarua'), ('Kericho', 'Kericho'), ('Kwale', 'Kwale'), ('Wajir', 'Wajir'), ('Kajiado', 'Kajiado'), ('Laikipia', 'Laikipia'), ('Siaya', 'Siaya'), ('Garissa', 'Garissa'), ('Mombasa', 'Mombasa'), ('Turkana', 'Turkana'), ('Baringo', 'Baringo'), ('Bomet', 'Bomet'), ('Makueni', 'Makueni'), ('Nyeri', 'Nyeri'), ('Lamu', 'Lamu'), ('Meru', 'Meru'), ('Nairobi', 'Nairobi'), ('Machakos', 'Machakos'), ('Migori', 'Migori'), ('Kakamega', 'Kakamega'), ('Taita-Taveta', 'Taita-Taveta'), ('Nakuru', 'Nakuru'), ('Kilifi', 'Kilifi'), ('Vihiga', 'Vihiga'), ('Embu', 'Embu'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Nandi', 'Nandi'), ('Busia', 'Busia'), ("Murang'a", 'Murang'), ('Samburu', 'Samburu'), ('Tana River', 'Tana River'), ('Uasin Gishu', 'Uasin Gishu'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Trans Nzoia', 'Trans Nzoia'), ('West Pokot', 'West Pokot'), ('Isiolo', 'Homa Bay'), ('Mandera', 'Mandera')], max_length=15),
        ),
        migrations.AlterField(
            model_name='blooddrives',
            name='drive_id',
            field=models.CharField(default=uuid.UUID('7072f8e9-91ae-478e-a688-444ea653f017'), max_length=20, primary_key=True, serialize=False),
        ),
    ]
