from django.urls import path
from . import views


app_name = "houses_api"


urlpatterns = [
    path("additional", views.AdditionalListView.as_view(), name="additional_list"),
    path("", views.HouseListView.as_view(), name="house_list"),
    path("detail/<id>/", views.HouseDetailView.as_view(), name="house_detail"),
    path("create/", views.HouseOrderCreateView.as_view(), name="house_order_create"),
    path("review/create/", views.HouseReviewCreateView.as_view(), name="house_review_create"),
    path("wishlist/", views.WishlistView.as_view(), name="house_wishlist"),
    path("wishlist/create/", views.WishlistCreateView.as_view(), name="house_wishlist_create"),
    path("category/", views.CategoryListView.as_view(), name="category"),
]