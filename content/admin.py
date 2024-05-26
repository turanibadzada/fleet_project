from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import (
    News, NewsImage, Event, EventImages, Category, 
    Additional, EventReview, EventOrder, Wishlist)


class NewsAdmin(TranslationAdmin):
    list_display = ("title", )


class CategoryAdmin(TranslationAdmin):
    list_display = ("name", )


class AdditionalAdmin(TranslationAdmin):
    list_display = ("name", )


class EventAdmin(TranslationAdmin):
    list_display = (
        "hosted_by", 
        "title", 
        "price"
    )



admin.site.register(News, NewsAdmin)
admin.site.register(NewsImage)
admin.site.register(Event, EventAdmin)
admin.site.register(EventImages)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Additional, AdditionalAdmin)
admin.site.register(EventReview)
admin.site.register(EventOrder)
admin.site.register(Wishlist)
