from django.db import models
from services.generator import CodeGenerator
from services.choices import GENDER_CHOICES
from .managers import MyUserManager
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)


def upload_to(instance, filename):
    return f"users/{instance.email}/{filename}"


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=120)
    name = models.CharField(max_length=250, blank=True, null=True)
    surname = models.CharField(max_length=250, blank=True, null=True)
    bio = models.CharField(max_length=250, blank=True, null=True)
    logo = models.ImageField(upload_to=upload_to, blank=True, null=True)
    profile_photo = models.ImageField(upload_to=upload_to, blank=True, null=True)
    mobile = PhoneNumberField(blank=True, null=True)
    gender = models.CharField(max_length=25, blank=True, null=True, choices=GENDER_CHOICES)
    location = CountryField()
    social = models.URLField(blank=True, null=True)

    slug = models.SlugField(unique=True)
    activation_code = models.CharField(max_length=6, blank=True, null=True)

    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"

    class Meta:
        ordering = ["-timestamp"]
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email

    def full_name(self):
        return f"{self.name} {self.surname}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = CodeGenerator.create_slug_shortcode(size=20, model_=self.__class__)
        if not self.logo:
            default_logo_path = "static/user/user.jpg"
            self.logo.save("default_user_logo.jpg", open(default_logo_path, "rb"), save=False)
        return super(User, self).save(*args, **kwargs)



