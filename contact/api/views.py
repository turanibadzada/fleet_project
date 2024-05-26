from rest_framework import generics
from ..models import AboutUs, ContactUs, Community, Support
from .serializers import (
    AboutUsSerializer, ContactUsSerializer, 
    CommunitySerializer, SupportSerializer)


class AboutUsView(generics.RetrieveAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

    def get_object(self):
        return self.queryset.first()



class ContactUsView(generics.CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer



class CommunityView(generics.CreateAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    


class SupportView(generics.CreateAPIView):
    queryset = Support.objects.all()
    serializer_class = SupportSerializer