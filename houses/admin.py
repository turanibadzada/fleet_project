from django.contrib import admin
from . models import Category, Additional, House, HouseImage, HouseReview, HouseOrder, Wishlist
from modeltranslation.admin import TranslationAdmin

class AdditionalAdmin(TranslationAdmin):
    list_display = ("name", )

class CategoryAdmin(TranslationAdmin):
    list_display = ("name", )


class HouseAdmin(TranslationAdmin):
    list_display = (
        "hosted_by",
        "address",
        "description",
        "price",
    )

    list_filter = (
        "hosted_by__is_staff",
    )


    
admin.site.register(Additional, AdditionalAdmin)
admin.site.register(House, HouseAdmin)
admin.site.register(HouseImage)
admin.site.register(HouseReview)
admin.site.register(Category, CategoryAdmin)
admin.site.register(HouseOrder)
admin.site.register(Wishlist)


