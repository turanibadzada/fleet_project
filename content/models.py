from django.db import models
from services.mixin import DateMixin
from ckeditor.fields import RichTextField
from services.uploader import Uploader
from countries.models import Countries
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth import get_user_model
from services.choices import RATING
from payment.models import Payment
from phonenumber_field.modelfields import PhoneNumberField


User = get_user_model()


class News(DateMixin):
    title = models.CharField(max_length=500)
    content = RichTextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"



class NewsImage(DateMixin):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=Uploader.news_image_uploader)

    def __str__(self):
        return self.news.title
    
    class Meta:
        verbose_name = "News Image"
        verbose_name_plural = "News Images"



class Category(MPTTModel):
    name = models.CharField(max_length=250)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name="children")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"



class Additional(DateMixin):
    name = models.CharField(max_length=150)
    icon = models.ImageField(upload_to=Uploader.event_additional_uploader)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Additional"
        verbose_name_plural = "Additionals"



class Event(DateMixin):
    hosted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    activity = RichTextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.IntegerField()
    discount_price = models.IntegerField()
    location = models.ForeignKey(Countries, on_delete=models.CASCADE)
    max_attendees = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    additionals = models.ManyToManyField(Additional, blank=True)
    location_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    @property
    def total_price(self):
        discount_price = self.price * (self.status or 0) / 100
        discounted_price = self.price - discount_price
        return round(float(discounted_price), 2)
    
    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    

class EventImages(DateMixin):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=Uploader.event_image_uploader)

    def __str__(self):
        return self.event.title
    
    class Meta:
        verbose_name = "Event Image"
        verbose_name_plural = "Event Images"



class EventReview(DateMixin, MPTTModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=RATING)
    message = models.TextField()
    parent = TreeForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name="children")

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = "Event Review"
        verbose_name_plural = "Event Reviews"



class EventOrder(DateMixin):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    mobile = PhoneNumberField()
    email = models.EmailField(max_length=250)
    password_series = models.CharField(max_length=250)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}"
    
    class Meta:
        verbose_name = "Event Order"
        verbose_name_plural = "Event Orders"



class Wishlist(DateMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="User")
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
    
    class Meta:
        verbose_name = "List"
        verbose_name_plural = "Wishlist"

