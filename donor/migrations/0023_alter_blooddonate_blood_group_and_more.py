# Generated by Django 4.2.3 on 2023-07-17 08:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0022_alter_blooddonate_blood_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddonate',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('O-', 'O-'), ('O+', 'O+'), ('AB+', 'AB+'), ('A', 'A'), ('AB-', 'AB-'), ('B-', 'B-'), ('B+', 'B+')], max_length=3),
        ),
        migrations.AlterField(
            model_name='blooddonate',
            name='donation_id',
            field=models.CharField(default=uuid.UUID('2486983f-dfc9-4a30-8411-68d3e0371e14'), max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='blooddonate',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Approved', 'Approved')], default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='donationtype',
            name='type',
            field=models.CharField(choices=[('Blood', 'Blood'), ('Platelets', 'Platelets'), ('Plasma', 'Plasma'), ('Power Red', 'Power Red')], default='Blood', max_length=10),
        ),
        migrations.AlterField(
            model_name='donor',
            name='bloodgroup',
            field=models.CharField(choices=[('A+', 'A+'), ('O-', 'O-'), ('O+', 'O+'), ('AB+', 'AB+'), ('A', 'A'), ('AB-', 'AB-'), ('B-', 'B-'), ('B+', 'B+')], max_length=10),
        ),
        migrations.AlterField(
            model_name='donor',
            name='donor_id',
            field=models.CharField(default=uuid.UUID('bb222595-4025-4537-ad87-6f4120debd3d'), max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='donor',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Approved', 'Approved')], default='Pending', max_length=8),
        ),
        migrations.AlterField(
            model_name='donorhealthinfo',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('O-', 'O-'), ('O+', 'O+'), ('AB+', 'AB+'), ('A', 'A'), ('AB-', 'AB-'), ('B-', 'B-'), ('B+', 'B+')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='donorhealthinfo',
            name='gender',
            field=models.CharField(choices=[('F', 'F'), ('M', 'M'), ('Nil', 'Nil')], default='Nil', max_length=3),
        ),
        migrations.AlterField(
            model_name='preexaminfo',
            name='pre_exam_id',
            field=models.CharField(default=uuid.UUID('0150a36f-7fe1-4de0-a9c0-23010cca7361'), max_length=10, primary_key=True, serialize=False),
        ),
    ]
