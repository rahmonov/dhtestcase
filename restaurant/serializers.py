from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Restaurant


class RestaurantSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
        geo_field = 'delivery_area'
