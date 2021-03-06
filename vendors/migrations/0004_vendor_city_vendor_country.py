# Generated by Django 4.0.2 on 2022-02-03 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('vendors', '0003_rename_location_vendor_lat_vendor_long'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='city',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.city'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='country',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.country'),
        ),
    ]
