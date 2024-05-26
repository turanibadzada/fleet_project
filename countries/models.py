from django.db import models
from services.mixin import DateMixin
from services.uploader import Uploader
from mptt.models import MPTTModel, TreeForeignKey


def country_uploader_image(instance, filename):
    return f"countries/{instance.name}/{filename}"

 
class Countries(DateMixin, MPTTModel):
    name = models.CharField(max_length=150)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, blank=True, null=True, related_name="children")
    image = models.ImageField(upload_to=country_uploader_image)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"




    