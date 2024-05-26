from django.urls import path
from . import views

app_name = "countries_api"

urlpatterns = [
    path("", views.CountriesListView.as_view(), name="countries_list")
]