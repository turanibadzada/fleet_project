from django.contrib import admin
from . models import Company, TicketSales, TicketOrder, Wishlist
from modeltranslation.admin import TranslationAdmin


class CompanyAdmin(TranslationAdmin):
    list_display = (
        "name", 
        "description", 
        "company_location"
    )


class TicketSalesAdmin(TranslationAdmin):
    list_display = (
        "description",
        "departure_country", 
        "destination_country"
    )


admin.site.register(Company, CompanyAdmin)
admin.site.register(TicketSales, TicketSalesAdmin)
admin.site.register(TicketOrder)
admin.site.register(Wishlist)
