from django.urls import path
from . import views


app_name = "flights_api"


urlpatterns = [
    path("", views.TicketSalesListView.as_view(), name="ticket_sales_list"),
    path("create/", views.TicketOrderCreateSerializer.as_view(), name="ticket_order_create"),
    path("detail/<id>/", views.TicketDetailView.as_view(), name="ticket_detail"),
    path("wishlist/", views.WishlistView.as_view(), name="ticket_wishlist"),
    path("wishlist/create/", views.WishlistCreateView.as_view(), name="ticket_wishlist_create"),
]