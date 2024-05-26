
from django.urls import path
from . import views

app_name = "notifications_api"

urlpatterns = [
    path("", views.NotificationListView.as_view(), name="notification_list"),
    path("detail/<id>/", views.NotificationDetailView.as_view(), name="notification_detail"),
    path("delete/<id>/", views.NotificationDeleteView.as_view(), name="notification_delete"),
]
