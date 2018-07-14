from django.urls import path

from .views import HomeView, OptimizeDeliveryAreasAPIView, RestaurantCreateAPIView

app_name = 'restaurant'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('restaurants/', RestaurantCreateAPIView.as_view(), name='restaurants'),
    path('restaurants/optimize/', OptimizeDeliveryAreasAPIView.as_view(), name='optimize-delivery-areas')
]
