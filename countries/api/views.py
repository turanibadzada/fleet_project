from rest_framework import generics
from . serializer import CountriesListSerializer
from . .models import Countries
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CountriesFilter


class CountriesListView(generics.ListAPIView):
    queryset = Countries.objects.all()
    serializer_class = CountriesListSerializer
    filter_backends = (
        DjangoFilterBackend,
    )
    filterset_class = CountriesFilter
 
