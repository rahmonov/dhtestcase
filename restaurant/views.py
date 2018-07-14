from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Restaurant
from .serializers import RestaurantSerializer
from .services import optimize


class HomeView(TemplateView):
    template_name = 'restaurant/home.html'


class RestaurantCreateAPIView(APIView):
    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        restaurant = serializer.save()

        return Response(restaurant.pk, status=status.HTTP_200_OK)

    def get(self, *args, **kwargs):
        restaurants = Restaurant.objects.all()

        serializer = RestaurantSerializer(restaurants, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class OptimizeDeliveryAreasAPIView(APIView):
    def post(self, request):
        optimize()

        return Response(status=status.HTTP_200_OK)
