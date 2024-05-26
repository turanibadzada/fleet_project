from modeltranslation.translator import TranslationOptions, translator
from .models import House, Category, Additional


class CategoryTranslationOptions(TranslationOptions):
    fields = ("name", )



class AdditionalTranslationOptions(TranslationOptions):
    fields = ("name", )



class HouseTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "description", 
    )

    
translator.register(Category, CategoryTranslationOptions)
translator.register(Additional, AdditionalTranslationOptions)
translator.register(House, HouseTranslationOptions)

