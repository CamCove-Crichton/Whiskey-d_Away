# Generated by Django 3.2.21 on 2023-09-20 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0004_alter_tours_tour_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='tours',
            options={'verbose_name_plural': 'Tours'},
        ),
    ]