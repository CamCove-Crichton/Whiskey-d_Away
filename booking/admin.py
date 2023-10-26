# Assistance from CI - Boutique Ado walkthrough
from django.contrib import admin
from .models import Booking, BookingItem


class BookingItemAdminInline(admin.TabularInline):
    model = BookingItem
    readonly_fields = ('lineitem_total',)


class BookingAdmin(admin.ModelAdmin):
    inlines = (BookingItemAdminInline,)

    readonly_fields = ('booking_number', 'date_of_booking',
                       'discount_amount', 'booking_total',
                       'grand_total', 'original_basket',
                       'stripe_pid')

    fields = ('booking_number', 'user_profile',
              'date_of_booking', 'first_name',
              'last_name', 'mobile_number',
              'email', 'date_of_birth', 'booking_total',
              'discount_amount', 'grand_total',
              'original_basket', 'stripe_pid')

    list_display = ('booking_number', 'date_of_booking',
                    'first_name', 'last_name', 'booking_total',
                    'discount_amount', 'grand_total')

    ordering = ('-date_of_booking',)


admin.site.register(Booking, BookingAdmin)
