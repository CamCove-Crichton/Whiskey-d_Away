# Generated by Django 3.2.21 on 2023-10-11 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_booking_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='test',
        ),
    ]