# Generated by Django 3.0.5 on 2023-07-15 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0004_auto_20230714_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='bloodgroup',
            field=models.CharField(choices=[('AB-', 'AB-'), ('A', 'A'), ('B+', 'B+'), ('O+', 'O+'), ('A+', 'A+'), ('B-', 'B-'), ('AB+', 'AB+'), ('O-', 'O-')], max_length=10),
        ),
        migrations.AlterField(
            model_name='donor',
            name='mobile',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
