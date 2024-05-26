import django_filters
from ..models import Countries

class CountriesFilter(django_filters.FilterSet):

    country = django_filters.ModelChoiceFilter(field_name="country", label="Country", queryset=Countries.objects.all())

    class Meta:
        model = Countries
        fields = ("country", )