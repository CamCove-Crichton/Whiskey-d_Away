from django.db import models
from django.core.validators import MaxLengthValidator
from .validators import (
    validate_country,
    validate_image_size,
    validate_img_extension
)


# Assistance from CI - Boutique Ado walkthrough
class Category(models.Model):
    """
    A model to store tours into categories should they be need to be
    categorized
    """

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=100)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Tours(models.Model):
    """
    A model to capture and store all information pertaining to the tour
    experiences on offer
    """
    # Assistance from CI - Boutique Ado walkthrough
    class Meta:
        verbose_name_plural = 'Tours'
    tour_category = models.ManyToManyField(
        Category, blank=True, related_name='tours',
        help_text="Hold ctrl/cmd key to select more than one")
    tour_name = models.CharField(max_length=100)
    # Assistance from ChatGPT
    tour_description = models.TextField(
        default="No description available",
        verbose_name="Tour Experience Description",
        validators=[MaxLengthValidator(
            limit_value=500, message="Description is too long.")])
    tour_price = models.DecimalField(max_digits=10, decimal_places=2)
    tour_image = models.ImageField(
        upload_to='tours/', null=True, blank=True,
        default="default whiskey experience.jpg",
        validators=[validate_image_size, validate_img_extension])
    # Assistance from CI - Boutique Ado walkthrough
    tour_rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    street_address1 = models.CharField(max_length=25)
    street_address2 = models.CharField(max_length=25, null=True, blank=True)
    town_or_city = models.CharField(max_length=60, null=True, blank=True)
    county = models.CharField(max_length=50, null=True, blank=True)
    post_code = models.CharField(max_length=10)
    country = models.CharField(max_length=10, validators=[validate_country])
    # Assitance from ChatGPT
    max_attendees = models.PositiveIntegerField(default=4, choices=[
        (2, '2'), (4, '4'), (6, '6'), (8, '8'),],
        help_text="Maximum number of attendees per group")
    max_capacity = models.PositiveIntegerField(
        default=12, choices=[(8, '8'), (12, '12'), (16, '16'), (20, '20'),],
        help_text="Maximum capacity per experience")

    def __str__(self):
        return self.tour_name
