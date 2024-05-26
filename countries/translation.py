from modeltranslation.translator import TranslationOptions, translator
from .models import Countries


class CountriesOption(TranslationOptions):
    fields = ("name", )


translator.register(Countries, CountriesOption)