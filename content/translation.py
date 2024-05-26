from modeltranslation.translator import TranslationOptions, translator
from .models import News, Category, Additional, Event

class NewsTranslationOptions(TranslationOptions):
    fields = ("title", "content")


class CategoryTranslationOptions(TranslationOptions):
    fields = ("name", )


class AdditionalTranslationOptions(TranslationOptions):
    fields = ("name", )


class EventTranslationOptions(TranslationOptions):
    fields = ("title", "activity")


translator.register(News, NewsTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Additional, AdditionalTranslationOptions)
translator.register(Event, EventTranslationOptions)