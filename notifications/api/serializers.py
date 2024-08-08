from rest_framework import serializers
from ..models import Notification


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = (
            "id",
            "content",
            "read",
        )



class NotificationDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = (
            "id",
            "content",
        )