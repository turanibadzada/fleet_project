from rest_framework import serializers
from . .models import Car, CarImage, CarReview, Countries, CarOrder, Category, Additional, Wishlist
from django.db.models import F, Avg, Count
from accounts.api.serializer import UserSeriazlier
from content.api.serializers import CountriesSerializer


class CarImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarImage
        fields = ("image", )



class CarReviewSerializer(serializers.ModelSerializer):
    user = UserSeriazlier(read_only=True)

    class Meta:
        model = CarReview
        fields = (
            "rating", 
            "user", 
            "message",
            "car",
        )
        extra_kwargs = {
            "car":{"write_only":True}
        }

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        reviews_list = instance.children.all()
        if reviews_list:
            repr_["replies"] = CarReviewSerializer(
            reviews_list, many=True
            ).data
        return repr_

    

class CarsCategorySerializer(serializers.ModelSerializer):

    class Meta: 
        model = Category
        fields = ("id", "name")



class AdditionalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Additional
        fields = ("name",)



class CarListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    total_price = serializers.IntegerField()
    rating = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    location = CountriesSerializer()

    class Meta:
        model = Car
        fields = (
            "model",
            "rent_per_day",
            "discount_interest",
            "location",
            "image",
            "total_price",
            "rating",
            "review_count",
        )

    def get_image(self, obj):
        image = obj.carimage_set.first()
        return CarImageSerializer(image).data

    def get_rating(self, obj):
        rating = (obj.carreview_set.aggregate(rating_=Avg(F("rating")))["rating_"])
        return rating

    def get_review_count(self, obj):
        count = obj.carreview_set.count()
        return count
 
    

class CarDetailSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    category = CarsCategorySerializer()
    additional = serializers.SerializerMethodField()
    hosted_by = serializers.SerializerMethodField()
    location = CountriesSerializer()

    class Meta:
        model = Car
        fields = (
            "id",
            "hosted_by",
            "model",
            "category",
            "location",
            "seating_capacity",
            "rent_per_day",
            "discount_interest",
            "additional",
            "activity",
            "protection",
            "image",
        )
   
    def get_image(self, obj):
        image = obj.carimage_set.all()
        return CarImageSerializer(image, many=True). data    

    def get_additional(self, obj):
        additional = obj.additional.all()
        return AdditionalSerializer(additional, many=True).data
    
    def get_hosted_by(self, obj):
        return f"{obj.hosted_by.name} {obj.hosted_by.surname}"

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        repr_["reviews"] = CarReviewSerializer(
            CarReview.objects.filter(parent__isnull=True, car=instance), many=True
        ).data
        return repr_
    
    
        

class CarOrderSerializer(serializers.ModelSerializer):
    car_model = serializers.SerializerMethodField()
    payment_card = serializers.SerializerMethodField()

    class Meta:
        model = CarOrder
        fields = (
            "name",
            "surname",
            "mobile",
            "email",
            "password_series",
            "car",
            "rental_date",
            "delivery_date",
            "payment",
            "car_model",
            "payment_card",
        )
        extra_kwargs = {
            "car" : {"write_only":True},
            "payment" : {"write_only":True},
        }
       
    def get_car_model(self, obj):
        return obj.car.model
    
    def get_payment_card(self, obj):
        return obj.payment.card


class CarWishlistSerializer(serializers.ModelSerializer):
    car_model = serializers.SerializerMethodField()
    car_seating_capacity = serializers.SerializerMethodField()
    car_additional = serializers.SerializerMethodField()
    car_image = serializers.SerializerMethodField()
    car_rent_per_day = serializers.SerializerMethodField()
    car_total_price = serializers.SerializerMethodField()
    car_category = serializers.SerializerMethodField()
    car_discount_interest = serializers.SerializerMethodField()
    car_images = serializers.SerializerMethodField()

    class Meta:
        model = Wishlist
        fields = (
            "car",
            "car_id",
            "car_model",
            "car_seating_capacity",
            "car_additional",
            "car_image",
            "car_rent_per_day",
            "car_total_price",
            "car_category",
            "car_discount_interest",
            "car_images",
        )
        extra_kwargs = {
            "car": {"write_only": True},
            "user": {"write_only": True}
        }

    def get_car_model(self, obj):
        return obj.car.model
    
    def get_car_seating_capacity(self, obj):
        return obj.car.seating_capacity
    
    def get_car_additional(self, obj):
        return AdditionalSerializer(obj.car.additional.all(), many=True).data
    
    def get_car_image(self, obj):
        image = obj.car.carimage_set.first()
        return CarImageSerializer(image).data

    def get_car_rent_per_day(self, obj):
        return obj.car.rent_per_day
    
    def get_car_total_price(self, obj):
        return obj.car.total_price
    
    def get_car_category(self, obj):
        return CarsCategorySerializer(obj.car.category).data

    def get_car_discount_interest(self, obj):
        return obj.car.discount_interest
   
    def get_car_images(self, obj):
        images = CarImage.objects.filter(car=obj.car)
        return CarImageSerializer(images, many=True).data
    
     
        