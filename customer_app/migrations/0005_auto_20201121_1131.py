# Generated by Django 3.1.2 on 2020-11-21 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer_app', '0004_auto_20201111_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='aadhar_card',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
    ]
