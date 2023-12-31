# Generated by Django 3.0.5 on 2023-07-15 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0012_auto_20230715_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='bloodgroup',
            field=models.CharField(choices=[('A', 'A'), ('AB-', 'AB-'), ('B+', 'B+'), ('O+', 'O+'), ('B-', 'B-'), ('AB+', 'AB+'), ('O-', 'O-'), ('A+', 'A+')], max_length=10),
        ),
        migrations.AlterField(
            model_name='donor',
            name='status',
            field=models.CharField(choices=[('Rejected', 'Rejected'), ('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=8),
        ),
    ]
