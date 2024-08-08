from django.db.models.signals import post_save
from .models import Notification
from cars.models import CarOrder
from houses.models import HouseOrder
from django.dispatch import receiver




@receiver(post_save, sender=CarOrder)
def create_car_order_notification(sender, instance, created, **kwargs):
    if created:
        notification_content = "Your car has been ordered"
        Notification.objects.create(
            user=instance.car.hosted_by,
            content=notification_content,
        )


@receiver(post_save, sender=HouseOrder)
def create_house_order_notification(sender, instance, created, **kwargs):
    if created:
        notification_content = "Your house has been ordered"
        Notification.objects.create(
            user=instance.house.hosted_by,
            content=notification_content,
        )

       