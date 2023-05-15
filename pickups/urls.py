from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pickup/', views.request_pickup, name='request_pickup'),
    path('receipt/<int:pickup_id>/', views.receipt, name='receipt'),
    path('reports/', views.reports, name='reports'),
]