# Generated by Django 4.2.3 on 2023-07-23 15:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0011_alter_donationreport_report_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationreport',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='reports/donation-reports/'),
        ),
        migrations.AlterField(
            model_name='donationreport',
            name='report_id',
            field=models.CharField(default=uuid.UUID('ed519c07-a13b-4e63-b042-d2d2e2cbd599'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='donorreport',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='reports/donor-reports/'),
        ),
        migrations.AlterField(
            model_name='donorreport',
            name='report_id',
            field=models.CharField(default=uuid.UUID('7af44b14-9f20-4016-a738-6ad6959942fb'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stationreport',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='reports/station-reports/'),
        ),
        migrations.AlterField(
            model_name='stationreport',
            name='report_id',
            field=models.CharField(default=uuid.UUID('1b714b36-4790-4b31-8a84-90ca8b532b55'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='stationreport',
            name='title',
            field=models.CharField(default='Station-report', max_length=100),
        ),
    ]
