import django_filters
from . .models import TicketSales
from countries.models import Countries

class TicketFilter(django_filters.FilterSet):
    departure_country = django_filters.ModelChoiceFilter(field_name="departure_country", queryset=Countries.objects.all())
    destination_country = django_filters.ModelChoiceFilter(field_name="destination_country", queryset=Countries.objects.all())
    departure_time = django_filters.RangeFilter(field_name="departure_time")
    arrivel_time = django_filters.RangeFilter(field_name="arrivel_time")
    parking_areas = django_filters.CharFilter(field_name="parking_areas")
    people_count = django_filters.RangeFilter(field_name="people_count")
    children_count = django_filters.RangeFilter(field_name="children_count")
    price = django_filters.RangeFilter(field_name="price", label="Price_range")

    class Meta:
        model = TicketSales
        fields = (
            "departure_country",
            "destination_country",
            "departure_time",
            "arrivel_time",
            "parking_areas",
            "price",
        )
