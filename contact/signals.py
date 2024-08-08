from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Community
from houses.models import House

@receiver(post_save, sender=House)
def send_mail_to_community(sender, instance, created, **kwargs):
    if not created:
        if instance.discount_interest:
            email_list = Community.objects.values_list("email", flat=True)
            if email_list:
                send_mail(
                    "Visit the site to view discounted homes",
                    "We have some houses with discounts. Check them out on our website.",
                    settings.EMAIL_HOST_USER,
                    list(email_list),  
                    fail_silently=False,
                )



