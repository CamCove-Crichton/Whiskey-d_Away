# Generated by Django 3.2.21 on 2023-09-28 04:43

import booking.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tours', '0010_tours_max_capacity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_number', models.CharField(editable=False, max_length=10, unique=True)),
                ('date_of_booking', models.DateField(auto_now_add=True)),
                ('grand_total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='BookingItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_attendees', models.IntegerField(default=1, validators=[booking.validators.validate_number_of_attendees])),
                ('booking_date', models.DateField()),
                ('booking_time_slot', models.CharField(choices=[('11:00-13:00', '11:00 AM - 1:00 PM'), ('13:00-15:00', '1:00 PM - 3:00 PM'), ('15:00-17:00', '3:00 PM - 5:00 PM')], max_length=11)),
                ('tour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='booking_items', to='tours.tours')),
            ],
        ),
    ]
