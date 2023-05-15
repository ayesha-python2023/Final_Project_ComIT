
#from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from .models import PickupRequest
from .forms import PickupRequestForm


SMALL_BOTTLE_REFUND = 0.10  # 10 cents
LARGE_BOTTLE_REFUND = 0.50  # 50 cents


def home(request):
    return render(request, 'home.html')


def request_pickup(request):
    if request.method == 'POST':
        form = PickupRequestForm(request.POST)
        if form.is_valid():
            pickup = form.save()
            return redirect('receipt', pickup_id=pickup.id)
        else:
            print(form.errors)
    else:
        form = PickupRequestForm()
    return render(request, 'pickup_form.html', {'form': form})

@login_required
def reports(request):
    pickup_requests = PickupRequest.objects.all()

    total_small_bottles = sum([pickup.small_bottles for pickup in pickup_requests])
    total_large_bottles = sum([pickup.large_bottles for pickup in pickup_requests])

    total_bottles = total_small_bottles + total_large_bottles

    total_refunds = (total_small_bottles * SMALL_BOTTLE_REFUND) + (total_large_bottles * LARGE_BOTTLE_REFUND)

    total_donations = sum([(pickup.small_bottles * SMALL_BOTTLE_REFUND * (pickup.donation_percentage/100)) +
                           (pickup.large_bottles * LARGE_BOTTLE_REFUND * (pickup.donation_percentage/100))
                           for pickup in pickup_requests])

    return render(request, 'reports.html', {
        'total_bottles': total_bottles,
        'total_refunds': total_refunds,
        'total_donations': total_donations
    })


def receipt(request, pickup_id):
    pickup = get_object_or_404(PickupRequest, pk=pickup_id)
    return render(request, 'receipt.html', {'pickup': pickup})
