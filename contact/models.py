
from django.db import models
from services.mixin import DateMixin
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model


User = get_user_model()



class AboutUs(DateMixin):
    title = models.CharField(max_length=250)
    about = RichTextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "About"
        verbose_name_plural = "AboutUs"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.__class__.objects.exclude(id=self.id).delete()



class ContactUs(DateMixin):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=250)
    contact_person = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "ContactUs"


    
class Community(DateMixin):
    email = models.EmailField(unique=True, max_length=100)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Community"
        verbose_name_plural = "Communities"



class Support(DateMixin):
    email = models.EmailField(max_length=100)
    mobile_call = PhoneNumberField()
    mobile_wp = PhoneNumberField()

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Support"
        verbose_name_plural = "Supports"