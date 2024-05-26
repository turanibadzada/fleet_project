from django.db import models
from django_countries.fields import CountryField
from countries.models import Countries
from services.mixin import DateMixin
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField
from services.choices import TICKET_STATUS_CHOICES, PARKING_AREAS_CHOICES, CLASS_OF_SERVİCES_CHOICES
from payment.models import Payment
from django.contrib.auth import get_user_model

User = get_user_model()


class Company(DateMixin):
    name = models.CharField(max_length=250)
    description = RichTextField()
    company_location = models.ForeignKey(Countries, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="photo/")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"



class TicketSales(DateMixin):
    description = RichTextField(null=True)
    departure_time = models.DateTimeField()
    arrivel_time = models.DateTimeField()
    price = models.IntegerField()
    departure_country = models.ForeignKey(Countries, on_delete=models.CASCADE, related_name="deptarture_country")
    destination_country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    parking_areas = models.CharField(max_length=100, choices=PARKING_AREAS_CHOICES)
    class_of_services = models.CharField(max_length=100, choices=CLASS_OF_SERVİCES_CHOICES)
    people_count = models.IntegerField()
    children_count = models.IntegerField(default=0)

    def __str__(self):
        return self.company.name
    
    class Meta:
        verbose_name_plural = "TicketSales"



class TicketOrder(DateMixin):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    status = models.CharField(max_length=250, choices=TICKET_STATUS_CHOICES)
    mobile = PhoneNumberField()
    email = models.EmailField(max_length=250)
    password_series = models.CharField(max_length=250)
    seat_number = models.CharField(max_length=250)
    ticket_sales = models.ForeignKey(TicketSales, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name} {self.surname}"
    
    class Meta:
        verbose_name = "Ticket Order"
        verbose_name_plural = "Ticket Orders"

    

class Wishlist(DateMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userr")
    ticketsales = models.ForeignKey(TicketSales, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = "List"
        verbose_name_plural = "Wishlist"





