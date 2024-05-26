import django_filters
from . .models import Car, Category

class CarFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(field_name="model", lookup_expr="icontains")
    category = django_filters.ModelChoiceFilter(field_name="category", queryset=Category.objects.all())
    delivery_location = django_filters.BooleanFilter(field_name="delivery_location")
    
    
    class Meta:
        model = Car
        fields = (
            "search",
            "category",
            "delivery_location"
        )

    def filter_queryset(self, queryset):
        category = self.form.cleaned_data.pop("category")
        queryset = super().filter_queryset(queryset)

        if category:
            queryset = queryset.filter(category__in=category.get_descendants(include_self=True))
        return queryset
    