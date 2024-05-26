from ..models import Notification
from rest_framework import generics
from rest_framework.response import Response
from .permission import NotificationPermission
from rest_framework.permissions import IsAuthenticated
from .serializers import NotificationSerializer, NotificationDetailSerializer

class NotificationListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user).order_by("created_at")
    


class NotificationDetailView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated, NotificationPermission)
    serializer_class = NotificationDetailSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)



class NotificationDeleteView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated, NotificationPermission)
    serializer_class = NotificationDetailSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Notification.objects.all()
    
