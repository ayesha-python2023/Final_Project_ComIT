from django import forms
from .models import PickupRequest

class PickupRequestForm(forms.ModelForm):
    class Meta:
        model = PickupRequest
        DONATION_CHOICES = (
        (0, '0%'),
        (10, '10%'),
        (20, '20%'),
        (30, '30%'),
        (40, '40%'),
        (50, '50%'),
        (60, '60%'),
        (70, '70%'),
        (80, '80%'),
        (90, '90%'),
        (100, '100%'),
    )
        small_bottles = forms.IntegerField(min_value=0, required=True)
        large_bottles = forms.IntegerField(min_value=0, required=True)
        pickup_date_time = forms.DateField(help_text="Bottles will be picked up between 8AM - 5PM on this date.")
        donation_percentage = forms.ChoiceField(choices=DONATION_CHOICES, initial=0)
        fields = ['name', 'address', 'email', 'phone_number', 'pickup_date_time', 'small_bottles', 'large_bottles', 'donation_percentage']