# Generated by Django 3.2.21 on 2023-10-16 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_auto_20231016_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]
