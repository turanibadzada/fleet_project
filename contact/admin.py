from django.contrib import admin
from .models import AboutUs, ContactUs, Community, Support, Privacy
from modeltranslation.admin import TranslationAdmin


class AboutUsAdmin(TranslationAdmin):
    list_display = ("title", "about")



class ContactUsAdmin(TranslationAdmin):
    list_display = ("subject", "message")



admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(Community)
admin.site.register(Support)
admin.site.register(Privacy)



