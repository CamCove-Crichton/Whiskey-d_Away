from django.apps import AppConfig


class BookingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booking'

    # Assistance from CI - Boutique Ado walkthrough
    def ready(self):
        import booking.signals
