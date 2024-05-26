from django.contrib import admin
from .models import Countries
from modeltranslation.admin import TranslationAdmin


class CountriesAdmin(TranslationAdmin):
    list_display = ("name", )


admin.site.register(Countries, TranslationAdmin)

