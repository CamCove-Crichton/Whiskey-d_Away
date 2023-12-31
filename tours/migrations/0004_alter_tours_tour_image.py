# Generated by Django 3.2.21 on 2023-09-19 06:39

from django.db import migrations, models
import tours.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0003_alter_tours_tour_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tours',
            name='tour_image',
            field=models.ImageField(blank=True, default='default whiskey experience.jpg', null=True, upload_to='tours/', validators=[tours.validators.validate_image_size, tours.validators.validate_img_extension]),
        ),
    ]
