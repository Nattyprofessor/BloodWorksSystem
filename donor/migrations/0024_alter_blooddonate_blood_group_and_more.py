# Generated by Django 4.2.3 on 2023-07-17 08:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0023_alter_blooddonate_blood_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddonate',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('B+', 'B+'), ('O-', 'O-'), ('B-', 'B-'), ('A', 'A'), ('O+', 'O+')], max_length=3),
        ),
        migrations.AlterField(
            model_name='blooddonate',
            name='donation_id',
            field=models.CharField(default=uuid.UUID('b8e60bb4-a50a-46c2-aaba-6916356567c8'), max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='blooddonate',
            name='status',
            field=models.CharField(choices=[('Rejected', 'Rejected'), ('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='donationtype',
            name='type',
            field=models.CharField(choices=[('Platelets', 'Platelets'), ('Blood', 'Blood'), ('Power Red', 'Power Red'), ('Plasma', 'Plasma')], default='Blood', max_length=10),
        ),
        migrations.AlterField(
            model_name='donor',
            name='bloodgroup',
            field=models.CharField(choices=[('A+', 'A+'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('B+', 'B+'), ('O-', 'O-'), ('B-', 'B-'), ('A', 'A'), ('O+', 'O+')], max_length=10),
        ),
        migrations.AlterField(
            model_name='donor',
            name='donor_id',
            field=models.CharField(default=uuid.UUID('fbb9a640-ae05-4ea0-b64a-0953b9f2f67e'), max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='donor',
            name='status',
            field=models.CharField(choices=[('Rejected', 'Rejected'), ('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=8),
        ),
        migrations.AlterField(
            model_name='donorhealthinfo',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('B+', 'B+'), ('O-', 'O-'), ('B-', 'B-'), ('A', 'A'), ('O+', 'O+')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='donorhealthinfo',
            name='gender',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F'), ('Nil', 'Nil')], default='Nil', max_length=3),
        ),
        migrations.AlterField(
            model_name='preexaminfo',
            name='pre_exam_id',
            field=models.CharField(default=uuid.UUID('de5cba09-aa97-4d28-8463-dfcb6cd26072'), max_length=10, primary_key=True, serialize=False),
        ),
    ]
