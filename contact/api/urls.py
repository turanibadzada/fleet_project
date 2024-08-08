from . import views
from django.urls import path


app_name = "contact_api"

urlpatterns = [
    path("about-us/", views.AboutUsView.as_view(), name="about_us"),
    path("contact-us/", views.ContactUsView.as_view(), name="contact_us"),
    path("community/", views.CommunityView.as_view(), name="community"),
    path("support/", views.SupportView.as_view(), name="support"),
    path("privacy/", views.PrivacyView.as_view(), name="privacy"),
]

    
