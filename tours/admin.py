# Assistance from CI - Boutique Ado walkthrough
from django.contrib import admin
from .models import Tours, Category


# Assistance from CI - Boutique Ado walkthrough
class ToursAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'tour_name',
        'display_categories',
        'tour_price',
        'tour_rating',
        'country',
        'tour_image',
    )

    def display_categories(self, obj):
        """
        A method to retrieve all the related categories, and join them
        using a comma separated string
        """
        return ", ".join(
            [category.name for category in obj.tour_category.all()])

    display_categories.short_description = 'Categories'

    ordering = ('id',)


# Assistance from CI - Boutique Ado walkthrough
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


# Assistance from CI - Boutique Ado walkthrough
admin.site.register(Tours, ToursAdmin)
admin.site.register(Category, CategoryAdmin)
