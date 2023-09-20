# Assistance from CI - Boutique Ado walkthrough
from django.contrib import admin
from .models import Tours, Category


# Assistance from CI - Boutique Ado walkthrough
class ToursAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'tour_name',
        'tour_category',
        'tour_price',
        'tour_rating',
        'country',
        'tour_image',
    )

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
