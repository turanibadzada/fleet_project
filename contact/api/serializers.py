from rest_framework import serializers
from ..models import AboutUs, ContactUs, Community, Support, Privacy




class AboutUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AboutUs
        fields = (
            "title", 
            "about",
        )



class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = (
            "full_name",
            "email",
            "subject",
            "message",
        )



class CommunitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Community
        fields = ("email", )

    def validate(self, attrs):
        email = attrs.get("email")

        if  Community.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error": "This email is already in use."})
        
        return super().validate(attrs)
    


class SupportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Support
        fields = (
            "email", 
            "mobile_call", 
            "mobile_wp",
        )



class PrivacySerializer(serializers.ModelSerializer):

    class Meta:
        model = Privacy
        fields = (
            "title",
            "description",
        )

