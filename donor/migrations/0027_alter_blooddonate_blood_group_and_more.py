# Generated by Django 4.2.3 on 2023-07-18 11:21

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0026_remove_blooddonate_date_blooddonate_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddonate',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('B-', 'B-'), ('O+', 'O+'), ('A+', 'A+'), ('O-', 'O-'), ('A', 'A'), ('B+', 'B+'), ('AB-', 'AB-'), ('AB+', 'AB+')], max_length=3),
        ),
        migrations.AlterField(
            model_name='blooddonate',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 18, 14, 21, 53, 186096)),
        ),
        migrations.AlterField(
            model_name='blooddonate',
            name='donation_id',
            field=models.CharField(default=uuid.UUID('5e12d8ec-6a36-421c-8fe2-08ce0e9a085f'), max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='blooddonate',
            name='status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='donationtype',
            name='type',
            field=models.CharField(choices=[('Blood', 'Blood'), ('Power Red', 'Power Red'), ('Platelets', 'Platelets'), ('Plasma', 'Plasma')], default='Blood', max_length=10),
        ),
        migrations.AlterField(
            model_name='donor',
            name='bloodgroup',
            field=models.CharField(choices=[('B-', 'B-'), ('O+', 'O+'), ('A+', 'A+'), ('O-', 'O-'), ('A', 'A'), ('B+', 'B+'), ('AB-', 'AB-'), ('AB+', 'AB+')], max_length=10),
        ),
        migrations.AlterField(
            model_name='donor',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 18, 14, 21, 53, 183099)),
        ),
        migrations.AlterField(
            model_name='donor',
            name='donor_id',
            field=models.CharField(default=uuid.UUID('76cedacd-cb6b-48e4-99a8-d9abba8f3f4f'), max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='donor',
            name='status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], default='Pending', max_length=8),
        ),
        migrations.AlterField(
            model_name='donorhealthinfo',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('B-', 'B-'), ('O+', 'O+'), ('A+', 'A+'), ('O-', 'O-'), ('A', 'A'), ('B+', 'B+'), ('AB-', 'AB-'), ('AB+', 'AB+')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='donorhealthinfo',
            name='gender',
            field=models.CharField(choices=[('F', 'F'), ('M', 'M'), ('Nil', 'Nil')], default='Nil', max_length=3),
        ),
        migrations.AlterField(
            model_name='preexaminfo',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 18, 14, 21, 53, 185097)),
        ),
        migrations.AlterField(
            model_name='preexaminfo',
            name='pre_exam_id',
            field=models.CharField(default=uuid.UUID('c1a7b887-1046-4052-ba50-841372d927db'), max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='preexaminfo',
            name='status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], default='Pending', max_length=8),
        ),
    ]
