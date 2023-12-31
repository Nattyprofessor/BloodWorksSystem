# Generated by Django 4.2.3 on 2023-07-17 16:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0032_alter_hostedblooddrives_county_and_more'),
        ('volunteer', '0003_alter_donationreport_report_id_donorreport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationreport',
            name='report_id',
            field=models.CharField(default=uuid.UUID('2ae54819-9e6a-4320-bc3b-2cf9f34801f3'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='donorreport',
            name='report_id',
            field=models.CharField(default=uuid.UUID('4eb09ffb-ebd2-4309-8679-8750fb03e105'), max_length=50, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='StationReport',
            fields=[
                ('report_id', models.CharField(default=uuid.UUID('0fcb0075-6f49-4517-a84f-3bdf93c1f4be'), max_length=50, primary_key=True, serialize=False)),
                ('station_id', models.CharField(default='x', max_length=50, null=True)),
                ('title', models.CharField(default='Donation-report', max_length=100)),
                ('file', models.FileField(blank=True, null=True, upload_to='reports/')),
                ('created_at', models.DateTimeField()),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.volunteerregistration')),
            ],
        ),
    ]
