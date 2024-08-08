from rest_framework import generics
from django.http import HttpResponse
from ..models import AboutUs, ContactUs, Community, Support, Privacy
from .serializers import (
    AboutUsSerializer, ContactUsSerializer, 
    CommunitySerializer, SupportSerializer, PrivacySerializer)
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
import io



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



class PrivacyView(generics.ListAPIView):
    queryset = Privacy.objects.all()
    serializer_class = PrivacySerializer

    
    def generate_pdfNew(self, request):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="privacy.pdf"'

        # PDF dokümanını oluşturun
        doc = SimpleDocTemplate(response, pagesize=letter)

        styles = getSampleStyleSheet()
        story = []


        privacy_objects = Privacy.objects.all()

        for privacy in privacy_objects:
            title = Paragraph(f"<strong>Title:</strong> {privacy.title}", styles['Title'])
            description = Paragraph(f"<strong>Description:</strong> {privacy.description}", styles['BodyText'])
            story.append(title)
            story.append(description)
            story.append(Spacer(1, 0.2 * inch))

        doc.build(story)

        return response

    
    def get(self, request, *args, **kwargs):
        response = self.generate_pdfNew(request)
        return response




   