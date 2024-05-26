from modeltranslation.translator import TranslationOptions, translator
from .models import AboutUs, ContactUs


class AboutUsTranslationOptions(TranslationOptions):
    fields = ("title", "about")



class ContactUsTranslationOptions(TranslationOptions):
    fields = ("subject", "message")



translator.register(AboutUs, AboutUsTranslationOptions)
translator.register(ContactUs, ContactUsTranslationOptions)