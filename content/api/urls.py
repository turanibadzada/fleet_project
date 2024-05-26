from django.urls import path
from .import views

app_name = "content_api"


urlpatterns = [
    path("news/", views.NewsListView.as_view(), name="News_list"),
    path("news/detail/<id>/", views.NewsDetailView.as_view(), name="News_detail"),
    path("event/", views.EventListView.as_view(), name="Event_list"),
    path("event/detail/<id>", views.EventDetailView.as_view(), name="Event_detail"),
    path("event/review/create/", views.EventReviewCreateView.as_view(), name="event_review_create"),
    path("event/wishlist/", views.WishlistView.as_view(), name="event_wishlist"),
    path("event/wishlist/create/", views.WishlistCreateView.as_view(), name="event_wishlist_create"),
    path("event/order/create/", views.EventOrderCreateView.as_view(), name="event_order_create")
]
