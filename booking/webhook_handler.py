# Assistance from CI - Boutique Ado walkthrough
from django.http import HttpResponse

from .models import Booking, BookingItem
from tours.models import Tours

import json
import time


class StripeWH_Handler:
    """
    Handle Stripe webhooks
    """
    def __init__(self, request):
        self.request = request
    
    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook
        from Stripe
        """
        intent = event.data.object
        pid = intent.id
        basket = intent.metdata.basket
        save_info = intent.metdata.save_info

        # Get the charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        grand_total = round(stripe_charge.amount / 100, 2)

        # Split billing detaails name value into first and last names
        # Assistance from ChatGPT
        full_name = billing_details.name
        first_name, *last_name_parts = full_name.split()
        last_name = ''.join(last_name_parts).strip()
        
        booking_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                booking = Booking.objects.get(
                    first_name__iexact=first_name,
                    last_name__iexact=last_name,
                    mobile_number__iexact=billing_details.phone,
                    email__iexact=billing_details.email,
                    grand_total=grand_total,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                booking_exists = True
                break
                
    
            except Booking.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if booking_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already exists in the database',
                status=200)
        else:
            booking = None
            try:
                booking = Booking.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    mobile_number=billing_details.phone,
                    email=billing_details.email,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(basket).items():
                    # Get the experience by id
                    experience = Tours.objects.get(id=item_id)

                    # Check if the item_data is a dictionary
                    if isinstance(item_data, dict):
                        number_of_attendees = (
                            item_data['number_of_attendees'])
                        booking_time_slot = (
                            item_data['booking_time_slot'])
                        booking_date = item_data['booking_date']
                        booking_line_item = BookingItem(
                            booking=booking,
                            tour=experience,
                            number_of_attendees=number_of_attendees,
                            booking_date=booking_date,
                            booking_time_slot=booking_time_slot,
                        )
                        booking_line_item.save()
            except Exception as e:
                if booking:
                    booking.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook
        from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200
        )
