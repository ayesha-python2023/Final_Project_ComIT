
from django.db import models

class PickupRequest(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    pickup_date_time = models.DateTimeField()
    small_bottles = models.IntegerField()
    large_bottles = models.IntegerField()
    donation_percentage = models.IntegerField(choices=[(i, f"{i}%") for i in [0, 10, 25, 50, 100]])
    status = models.CharField(max_length=20, default='pending', choices=[('pending', 'Pending'), ('in progress', 'In Progress'), ('completed', 'Completed')])

    @property
    def total_refund(self):
        return self.small_bottles * 0.10 + self.large_bottles * 0.50

    @property
    def donation_amount(self):
        return self.total_refund * (self.donation_percentage / 100.0)
