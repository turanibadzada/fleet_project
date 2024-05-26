from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from countries.models import Countries
from services.mixin import DateMixin
from ckeditor.fields import RichTextField
from services.uploader import Uploader
from services.choices import HOUSE_STATUS_CHOICES, RATING, ROOMS_COUNT_CHOICES
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from payment.models import Payment


User = get_user_model()

class Category(MPTTModel):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to=Uploader.category_image_uploader, blank=True, null=True)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name="children")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


    
class Additional(DateMixin):
    name = models.CharField(max_length=250)
    icon = models.ImageField(upload_to=Uploader.additional_image_uploader)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Additional"
        verbose_name_plural = "Additionals"



class House(DateMixin):
    hosted_by = models.ForeignKey(User,  on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=150)
    living_room = models.IntegerField(choices=ROOMS_COUNT_CHOICES)
    bed_room = models.IntegerField(choices=ROOMS_COUNT_CHOICES)
    bath_room = models.IntegerField(choices=ROOMS_COUNT_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Countries, on_delete=models.CASCADE, null=True)
    address = RichTextField()
    amenities = models.ManyToManyField(Additional, blank=True)
    discount_interest = models.IntegerField(blank=True, null=True, choices=HOUSE_STATUS_CHOICES)
    description = RichTextField()
    price = models.IntegerField()
    location_url = models.URLField(blank=True, null=True)
    people_count = models.IntegerField()
    children = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def total_price(self):
        discount_price = self.price * (self.status or 0) / 100
        discounted_price = self.price - discount_price
        return round(float(discounted_price), 2)
    
    class Meta:
        verbose_name = "House"
        verbose_name_plural = "Houses"



class HouseImage(DateMixin):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=Uploader.house_image_uploader)

    def __str__(self):
        return self.house.address
    
    class Meta:
        verbose_name = "House Image"
        verbose_name_plural = "House Images"
    
    

class HouseReview(DateMixin, MPTTModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=RATING)
    message = models.TextField()
    parent = TreeForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name="children")

    def __str__(self) -> str:
        return self.user.email

    class Meta:
        verbose_name = "House Review"
        verbose_name_plural = "House Reviews"
    


class HouseOrder(DateMixin):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    mobile = PhoneNumberField()
    email = models.EmailField(max_length=250)
    password_series = models.CharField(max_length=250)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    check_in = models.DateTimeField(blank=True, null=True)
    check_out = models.DateTimeField(blank=True, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = "House Order"
        verbose_name_plural = "House Orders"



class Wishlist(DateMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    house = models.ForeignKey(House, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = "List"
        verbose_name_plural = "Wishlist"









