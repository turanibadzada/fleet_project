from django.db import models
from services.mixin import DateMixin
from services.uploader import Uploader
from django.contrib.auth import get_user_model

User = get_user_model()


class Notification(DateMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    read = models.BooleanField(default=False)
    

    def __str__(self):
        return self.user.email 
    
    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"