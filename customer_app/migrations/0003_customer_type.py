# Generated by Django 3.1.2 on 2020-11-11 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_app', '0002_auto_20201031_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='type',
            field=models.CharField(choices=[('USER', 'user'), ('STAFF', 'staff')], default='USER', max_length=10),
        ),
    ]
