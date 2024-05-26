from rest_framework import serializers
from . .models import Countries


class CountriesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Countries
        fields = ("name", "image")

        