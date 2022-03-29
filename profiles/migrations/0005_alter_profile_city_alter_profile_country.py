# Generated by Django 4.0.2 on 2022-02-02 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('profiles', '0004_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.city'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.country'),
        ),
    ]