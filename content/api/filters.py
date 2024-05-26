import django_filters
from ..models import Category, Event, Countries


class EventFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(field_name="category", queryset=Category.objects.all())
    location = django_filters.ModelChoiceFilter(field_name="location", queryset=Countries.objects.all())

    class Meta:
        model = Event
        fields = (
            "category",
            "location",
        )

    def filter_queryset(self, queryset):
        category = self.form.cleaned_data.pop("category")
        queryset = super().filter_queryset(queryset)

        if category:
            queryset = queryset.filter(category__in=category.get_descendants(include_self=True))
        return queryset