from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from countries.models import Countries
from services.mixin import DateMixin
from services.choices import DISCOUNT_CHOICES
from ckeditor.fields import RichTextField
from services.uploader import Uploader
from services.choices import RATING
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model
from payment.models import Payment


User = get_user_model()


class Category(MPTTModel):
    name = models.CharField(max_length=250)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name="children")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"



class Additional(DateMixin):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Additional"
        verbose_name_plural = "Additionals"



class Car(DateMixin):
    hosted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    model = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Countries, on_delete=models.CASCADE, null=True)
    seating_capacity = models.IntegerField()
    rent_per_day = models.IntegerField()
    discount_interest = models.IntegerField(blank=True, null=True, choices=DISCOUNT_CHOICES)
    additional = models.ManyToManyField(Additional, blank=True)
    activity = RichTextField()
    protection = RichTextField()
    location_url = models.URLField(blank=True, null=True)
    delivery_location = models.BooleanField(default=False)
   
    def __str__(self):
        return self.model

    @property
    def total_price(self):
        discount_price = self.rent_per_day * (self.discount_interest or 0) / 100
        discounted_price = self.rent_per_day - discount_price
        return round(float(discounted_price), 2)
    
    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"



class CarImage(DateMixin):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=Uploader.car_image_uploader)

    def __str__(self) -> str:
        return self.car.model

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"



class CarReview(DateMixin, MPTTModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=RATING)
    message = models.TextField()
    parent = TreeForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name="children")

    def __str__(self) -> str:
        return self.user.email

    class Meta:
        verbose_name = "Car Review"
        verbose_name_plural = "Car Reviews"
    


class CarOrder(DateMixin):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    mobile = PhoneNumberField()
    email = models.EmailField(max_length=250)
    password_series = models.CharField(max_length=250)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rental_date = models.DateTimeField(blank=True, null=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)
    
    def __str__(self) -> str:
        return f"{self.name} {self.surname}"
    
    class Meta:
        verbose_name = "Car Order"
        verbose_name_plural = "Car Orders"



class Wishlist(DateMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = "List"
        verbose_name_plural = "Wishlist"




    

