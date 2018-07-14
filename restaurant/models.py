from django.contrib.gis.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    location = models.PointField()
    delivery_area = models.PolygonField()

    def __str__(self):
        return self.name
