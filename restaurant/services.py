from django.contrib.gis.db.models.functions import Translate

from restaurant.models import Restaurant


def optimize():
    overlap_found = False

    for r1 in Restaurant.objects.all():
        overlapping_restaurants = Restaurant.objects.filter(delivery_area__overlaps=r1.delivery_area)

        if overlapping_restaurants.exists():
            overlap_found = True

            for r2 in overlapping_restaurants:
                shift_direction = get_best_shift_direction(r1, r2)

                while r1.delivery_area.overlaps(r2.delivery_area):
                    r1.delivery_area = translate(r1, list(map(lambda x: x*2, shift_direction))).new_del_area
                    r1.save(update_fields=['delivery_area'])

    if overlap_found:
        optimize()


def get_best_shift_direction(r1, r2):
    directions = [
        (0, 0.0001), (0.00007, 0.00007),
        (0.0001, 0), (0.00007, -0.00007),
        (0, -0.0001), (-0.00007, -0.00007),
        (-0.0001, 0), (-0.00007, 0.00007)
    ]

    min_overlapping_area = r1.delivery_area.intersection(r2.delivery_area).area
    best_direction = directions[0]

    for direction in directions:
        translated_r = translate(r1, direction)
        new_overlapping_area = translated_r.new_del_area.intersection(r2.delivery_area).area

        if new_overlapping_area < min_overlapping_area:
            min_overlapping_area = new_overlapping_area
            best_direction = direction

    return best_direction


def translate(r, direction):
    return (
        Restaurant
        .objects
        .filter(pk=r.pk)
        .annotate(new_del_area=Translate('delivery_area', direction[0], direction[1])).first()
    )
