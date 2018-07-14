import pytest

from restaurant.models import Restaurant
from restaurant.services import optimize


@pytest.mark.django_db
def test_optimize(overlapping_restaurants):
    optimize()

    for r in Restaurant.objects.all():
        assert Restaurant.objects.filter(delivery_area__overlaps=r.delivery_area).exists() is False
