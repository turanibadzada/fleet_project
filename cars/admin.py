from django.contrib import admin
from . models import Category, Additional, Car, CarImage, CarReview, CarOrder, Wishlist
from modeltranslation.admin import TranslationAdmin


class CategoryAdmin(TranslationAdmin):
    list_display = ("name", )


class AdditionalAdmin(TranslationAdmin):
    list_display = ("name", )


class CarAdmin(TranslationAdmin):
    list_display = (
        "location",
        "activity",
        "protection",
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Additional, AdditionalAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(CarImage)
admin.site.register(CarReview)
admin.site.register(CarOrder)
admin.site.register(Wishlist)

