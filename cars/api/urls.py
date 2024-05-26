from django.urls import path
from . import views


app_name = "cars_api"


urlpatterns = [
    path("", views.CarListView.as_view(), name="car_list"),
    path("detail/<id>/", views.CarDetailView.as_view(), name="car_detail"),
    path("create/", views.CarOrderCreateView.as_view(), name="car_order_create"),
    path("review/create/", views.CarReviewCreateView.as_view(), name="car_review_create"),
    path("wishlist/", views.WishlistView.as_view(), name="car_wishlist"),
    path("wishlist/create/", views.WishlistCreateView.as_view(), name="car_wishlist_create"),
]