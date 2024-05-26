from django.db.models.signals import post_save
from .models import Community
from houses.models import House
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings


email_list = Community.objects.values_list("email", flat=True)


@receiver(post_save, sender=House)
def send_mail(sender, instance, created, **kwargs):

    if not created:
        if instance.discount_interest and email_list:
            send_mail(
                "Fleet",
                "endirimde olan evlere baxmag ucun sayta kecid edin",
                settings.EMAIL_HOST_USER,
                email_list,
                fail_silently=True,
            )
