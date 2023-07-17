# Generated by Django 3.0.5 on 2023-07-15 15:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0014_auto_20230715_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blooddrives',
            name='id',
        ),
        migrations.AlterField(
            model_name='blooddrives',
            name='county',
            field=models.CharField(choices=[('Uasin Gishu', 'Uasin Gishu'), ('Nandi', 'Nandi'), ('Meru', 'Meru'), ('Turkana', 'Turkana'), ('Isiolo', 'Homa Bay'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Samburu', 'Samburu'), ('Bomet', 'Bomet'), ('Kisii', 'Kisii'), ('Tana River', 'Tana River'), ('Lamu', 'Lamu'), ("Murang'a", 'Murang'), ('Homa Bay', 'Homa Bay'), ('Taita-Taveta', 'Taita-Taveta'), ('Nakuru', 'Nakuru'), ('Bungoma', 'Bungoma'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Wajir', 'Wajir'), ('Kiambu', 'Kiambu'), ('Kilifi', 'Kilifi'), ('Nyamira', 'Nyamira'), ('Migori', 'Migori'), ('Kitui', 'Kitui'), ('Laikipia', 'Laikipia'), ('Makueni', 'Makueni'), ('Kirinyaga', 'Kirinyaga'), ('Marsabit', 'Marsabit'), ('Mandera', 'Mandera'), ('Mombasa', 'Mombasa'), ('Nyeri', 'Nyeri'), ('Garissa', 'Garissa'), ('Machakos', 'Machakos'), ('Kajiado', 'Kajiado'), ('Busia', 'Busia'), ('Nyandarua', 'Nyandarua'), ('Trans Nzoia', 'Trans Nzoia'), ('Kisumu', 'Kisumu'), ('Siaya', 'Siaya'), ('Nairobi', 'Nairobi'), ('Baringo', 'Baringo'), ('Kericho', 'Kericho'), ('West Pokot', 'West Pokot'), ('Kakamega', 'Kakamega'), ('Vihiga', 'Vihiga'), ('Embu', 'Embu'), ('Kwale', 'Kwale'), ('Narok', 'Narok')], max_length=15),
        ),
        migrations.AlterField(
            model_name='blooddrives',
            name='drive_id',
            field=models.CharField(default=uuid.UUID('e1a53bca-4658-42c1-91c4-f0a82b4ea6fb'), max_length=20, primary_key=True, serialize=False),
        ),
    ]