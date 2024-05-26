from django.db import models
from services.mixin import DateMixin
from django.contrib.auth import get_user_model
from services.choices import CARD_TYPE_CHOICES


User = get_user_model()


class Payment(DateMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.CharField(max_length=20, choices=CARD_TYPE_CHOICES)
    number = models.IntegerField()
    date = models.CharField(max_length=10)
    cvc = models.IntegerField()
    message = models.CharField(max_length=30)

    def __str__(self):
        return self.card
    
    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"




