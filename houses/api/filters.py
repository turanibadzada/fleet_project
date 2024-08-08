import django_filters
from ..models import House, Category, Countries, HouseOrder
from django_filters import DateTimeFromToRangeFilter
from services.choices import GO_SOMEWHERE_STATUS


class HouseFilter(django_filters.FilterSet):
    total_price = django_filters.RangeFilter(field_name="totalprice", label="totalprice_range")
    category = django_filters.ModelChoiceFilter(field_name="category", queryset=Category.objects.all())
    location = django_filters.ModelChoiceFilter(field_name="location", queryset=Countries.objects.all())
    people_count = django_filters.RangeFilter(field_name="people_count", label="people_count_range")
    children = django_filters.RangeFilter(field_name="children", label="children_range")
    living_room = django_filters.RangeFilter(field_name="livin_groom", label="living_room_range")
    bath_room = django_filters.RangeFilter(field_name="bath_room", label="bath_room_range")
    bed_room = django_filters.RangeFilter(field_name="bed_room", label="bed_room_range")
    check_in = DateTimeFromToRangeFilter(field_name="houseorder__check_in", label="check_in_range")
    check_out = DateTimeFromToRangeFilter(field_name="houseorder__check_out", label="check_out_range")
    status = django_filters.ChoiceFilter(field_name="status", choices=GO_SOMEWHERE_STATUS)
    
    class Meta:
        model = House
        fields = (
            "total_price",
            "category",
            "location",
            "people_count",
            "children",
            "living_room",
            "bath_room",
            "bed_room",
            "check_in",
            "check_out",
            "status",
        )


    def filter_queryset(self, queryset):
        category = self.form.cleaned_data.pop("category")
        queryset = super().filter_queryset(queryset)

        if category:
            queryset = queryset.filter(category__in=category.get_descendants(include_self=True))
        return queryset
    

    

