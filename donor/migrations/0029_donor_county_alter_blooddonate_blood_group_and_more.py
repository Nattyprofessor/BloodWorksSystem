# Generated by Django 4.2.3 on 2023-07-23 15:28

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0028_alter_blooddonate_blood_group_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='county',
            field=models.CharField(choices=[('Meru', 'Meru'), ('Mombasa', 'Mombasa'), ('Tana River', 'Tana River'), ('Lamu', 'Lamu'), ('Marsabit', 'Marsabit'), ('Uasin Gishu', 'Uasin Gishu'), ('Embu', 'Embu'), ('Siaya', 'Siaya'), ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'), ('Kitui', 'Kitui'), ('Kajiado', 'Kajiado'), ('Bomet', 'Bomet'), ('West Pokot', 'West Pokot'), ('Isiolo', 'Homa Bay'), ('Tharaka-Nithi', 'Tharaka-Nithi'), ('Kwale', 'Kwale'), ('Kisumu', 'Kisumu'), ('Nyeri', 'Nyeri'), ('Garissa', 'Garissa'), ('Machakos', 'Machakos'), ('Migori', 'Migori'), ('Baringo', 'Baringo'), ('Kisii', 'Kisii'), ('Nairobi', 'Nairobi'), ('Turkana', 'Turkana'), ('Nyamira', 'Nyamira'), ('Trans Nzoia', 'Trans Nzoia'), ('Kericho', 'Kericho'), ('Nyandarua', 'Nyandarua'), ('Homa Bay', 'Homa Bay'), ('Busia', 'Busia'), ('Nakuru', 'Nakuru'), ('Kirinyaga', 'Kirinyaga'), ("Murang'a", "Murang'a"), ('Wajir', 'Wajir'), ('Nandi', 'Nandi'), ('Mandera', 'Mandera'), ('Laikipia', 'Laikipia'), ('Kakamega', 'Kakamega'), ('Narok', 'Narok'), ('Vihiga', 'Vihiga'), ('Kilifi', 'Kilifi'), ('Makueni', 'Makueni'), ('Bungoma', 'Bungoma'), ('Samburu', 'Samburu'), ('Kiambu', 'Kiambu'), ('Taita-Taveta', 'Taita-Taveta')], default='None', max_length=15),
        ),
        migrations.AlterField(
            model_name='blooddonate',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O-', 'O-'), ('AB-', 'AB-'), ('B-', 'B-'), ('A', 'A'), ('O+', 'O+')], max_length=3),
        ),
        migrations.AlterField(
            model_name='blooddonate',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 23, 18, 28, 20, 488539)),
        ),
        migrations.AlterField(
            model_name='blooddonate',
            name='donation_id',
            field=models.CharField(default=uuid.UUID('edbb2c2d-af59-4fd2-a131-8fb7f88fac4f'), max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='donationtype',
            name='type',
            field=models.CharField(choices=[('Power Red', 'Power Red'), ('Platelets', 'Platelets'), ('Blood', 'Blood'), ('Plasma', 'Plasma')], default='Blood', max_length=10),
        ),
        migrations.AlterField(
            model_name='donor',
            name='bloodgroup',
            field=models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O-', 'O-'), ('AB-', 'AB-'), ('B-', 'B-'), ('A', 'A'), ('O+', 'O+')], max_length=10),
        ),
        migrations.AlterField(
            model_name='donor',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 23, 18, 28, 20, 480545)),
        ),
        migrations.AlterField(
            model_name='donor',
            name='donor_id',
            field=models.CharField(default=uuid.UUID('007eed86-61d5-4091-b910-5f579c777d5d'), max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='donor',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile/Donor/default.png', null=True, upload_to='profile_pic/Donor/'),
        ),
        migrations.AlterField(
            model_name='donorhealthinfo',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O-', 'O-'), ('AB-', 'AB-'), ('B-', 'B-'), ('A', 'A'), ('O+', 'O+')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='donorhealthinfo',
            name='gender',
            field=models.CharField(choices=[('F', 'F'), ('Nil', 'Nil'), ('M', 'M')], default='Nil', max_length=3),
        ),
        migrations.AlterField(
            model_name='preexaminfo',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 23, 18, 28, 20, 484542)),
        ),
        migrations.AlterField(
            model_name='preexaminfo',
            name='pre_exam_id',
            field=models.CharField(default=uuid.UUID('33b7168d-2d86-498f-b2da-dc9a3403cf06'), max_length=10, primary_key=True, serialize=False),
        ),
    ]