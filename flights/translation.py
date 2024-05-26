from modeltranslation.translator import TranslationOptions, translator
from .models import Company, TicketSales


class CompanyTranslationOptions(TranslationOptions):
    fields = ("name", "description")


class TicketSalesTranslationOptions(TranslationOptions):
    fileds = ("description", "departure_country", "destination_country")




translator.register(Company, CompanyTranslationOptions)
translator.register(TicketSales, TicketSalesTranslationOptions)