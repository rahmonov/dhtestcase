from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('restaurant.urls', namespace='restaurant')),
    path('admin/', admin.site.urls),
]
