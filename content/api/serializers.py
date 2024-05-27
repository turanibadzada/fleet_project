from rest_framework import serializers
from accounts.api.serializer import UserSeriazlier
from ..models import (
    News, NewsImage, Event, EventImages, Category,
    Additional, EventReview, Wishlist, Countries, EventOrder)



class CountriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Countries
        fields = (
            "id", 
            "name", 
            "image",
        )



class NewsImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsImage
        fields = ("image", )



class NewsListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = (
            "id", 
            "image", 
            "title"
        )

    def get_image(self, obj):
        image = obj.newsimage_set.first()
        return NewsImageSerializer(image).data
    
    

class NewsDetailSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = (
            "id", 
            "title", 
            "images", 
            "content",
        )

    def get_images(self, obj):
        images = obj.newsimage_set.all()
        return NewsImageSerializer(images, many=True).data
    


class EventImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventImages
        fields = ("image", )     



class EventCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            "id", 
            "name",
        )



class AdditionalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Additional
        fields = (
            "id", 
            "name", 
            "icon"
        )



class EventReviewSerializer(serializers.ModelSerializer):
    user = UserSeriazlier(read_only=True)

    class Meta:
        model = EventReview
        fields = (
            "rating",
            "user",
            "message",
            "event",
        )
        extra_kwargs = {
            "event" : {"write_only": True}
        }

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        reviews_list = instance.children.all()
        if reviews_list:
            repr_["replies"] = EventReviewSerializer(
            reviews_list, many=True
            ).data
        return repr_



class EventListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    totalprice = serializers.IntegerField()
    rating = serializers.FloatField()
    review_count = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = (
            "id",
            "title",
            "max_attendees",
            "image",
            "price",
            "discount_price",
            "totalprice",
            "start_date",
            "end_date",
            "rating",
            "review_count",
        )

    def get_image(self, obj):
        image=obj.eventimages_set.first()
        return EventImagesSerializer(image).data
    
    def get_review_count(self, obj):
        count = obj.eventreview_set.count()
        return count
    


class EventDetailSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    category = EventCategorySerializer()
    additionals = serializers.SerializerMethodField()
    hosted_by = serializers.SerializerMethodField()
    location = CountriesSerializer()

    class Meta:
        model = Event
        fields = (
            "hosted_by",
            "title",
            "image",
            "activity",
            "start_date",
            "end_date",
            "price",
            "discount_price",
            "location",
            "max_attendees",
            "category",
            "additionals",
        )
    
    def get_image(self, obj):
        image = obj.eventimages_set.all()
        return EventImagesSerializer(image, many=True).data

    def get_additionals(self, obj):
        additionals = obj.additionals.all()
        return AdditionalSerializer(additionals, many=True).data
    
    def get_hosted_by(self, obj):
        return f"{obj.hosted_by.name} {obj.hosted_by.surname}"
    
    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        repr_["reviews"] = EventReviewSerializer(
            EventReview.objects.filter(parent__isnull=True, event=instance), many=True
        ).data
        return repr_
    


class EventOrderCreateSerializer(serializers.ModelSerializer):
    event_title = serializers.SerializerMethodField()
    payment_card = serializers.SerializerMethodField()
    
    class Meta:
        model = EventOrder
        fields = (
            "name",
            "surname",
            "mobile",
            "email",
            "password_series",
            "event",
            "payment",
            "event_title",
            "payment_card",
        )
        extra_kwargs = {
            "event" : {"write_only":True},
            "payment" : {"write_only":True},
        }

    def get_event_title(self, obj):
        return obj.event.title
    
    def get_payment_card(self, obj):
        return obj.payment.card
        


class EventWishlistSerializer(serializers.ModelSerializer):
    event_title = serializers.SerializerMethodField()
    event_activity = serializers.SerializerMethodField()
    event_start_date = serializers.SerializerMethodField()
    event_end_date = serializers.SerializerMethodField()
    event_price = serializers.SerializerMethodField()
    event_discount_price = serializers.SerializerMethodField()
    event_total_price = serializers.SerializerMethodField()
    event_location = serializers.SerializerMethodField()
    event_max_attendees = serializers.SerializerMethodField()
    event_additionals = serializers.SerializerMethodField()
    event_category = serializers.SerializerMethodField()
    event_images = serializers.SerializerMethodField()

    class Meta:
        model = Wishlist
        fields = (
            "event",
            "event_id",
            "event_title",
            "event_activity",
            "event_start_date",
            "event_end_date",
            "event_price",
            "event_discount_price",
            "event_total_price",
            "event_location",
            "event_max_attendees",
            "event_additionals",
            "event_category",
            "event_images",
        )
        extra_kwargs = {
            "event": {"write_only": True},
        }

    def get_event_title(self, obj):
        return obj.event.title
    
    def get_event_activity(self, obj):
        return obj.event.activity
    
    def get_event_start_date(self, obj):
        return obj.event.start_date
    
    def get_event_end_date(self, obj):
        return obj.event.end_date
    
    def get_event_price(self, obj):
        return obj.event.price
    
    def get_event_discount_price(self, obj):
        return obj.event.discount_price
    
    def get_event_total_price(self, obj):
        disc_price = obj.event.price * (obj.event.discount_price or 0) / 100
        return obj.event.price - disc_price
    
    def get_event_location(self, obj):
        return CountriesSerializer(obj.event.location).data
    
    def get_event_max_attendees(self, obj):
        return obj.event.max_attendees
    
    def get_event_additionals(self, obj):
        return AdditionalSerializer(obj.event.additionals.all(), many=True).data
    
    def get_event_category(self, obj):
        return EventCategorySerializer(obj.event.category).data
    
    def get_event_images(self, obj):
        images = EventImages.objects.filter(event=obj.event)
        return EventImagesSerializer(images, many=True).data
        
