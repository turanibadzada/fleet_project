from modeltranslation.translator import TranslationOptions, translator
from .models import Category, Additional, Car


class CategoryTranslationOptions(TranslationOptions):
    fields = ("name", )



class AdditionalTranslationOptions(TranslationOptions):
    fields = ("name", )



class CarTranslationOptions(TranslationOptions):
    fields = (
        "activity",
        "protection",
    )

    
translator.register(Category, CategoryTranslationOptions)
translator.register(Additional, AdditionalTranslationOptions)
translator.register(Car, CarTranslationOptions)