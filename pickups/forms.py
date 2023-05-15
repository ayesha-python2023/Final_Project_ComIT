from django import forms
from .models import PickupRequest

class PickupRequestForm(forms.ModelForm):
    class Meta:
        model = PickupRequest
        fields = ['name', 'address', 'email', 'phone_number', 'pickup_date_time', 'small_bottles', 'large_bottles', 'donation_percentage']
