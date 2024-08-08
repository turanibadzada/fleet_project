from rest_framework import serializers
from . .models import House, HouseImage, HouseReview, HouseOrder, Category, Additional, Countries, Wishlist
from accounts.api.serializer import UserSeriazlier
from content.api.serializers import CountriesSerializer



class HouseImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = HouseImage
        fields = ("image", )



class HouseReviewSerializer(serializers.ModelSerializer):
    user = UserSeriazlier(read_only=True)

    class Meta:
        model = HouseReview
        fields = (
            "rating",
            "user",
            "message",
            "house",
        )
        extra_kwargs = {
            "house":{"write_only":True}
        }
    

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        reviews_list = instance.children.all()
        if reviews_list:
            repr_["replies"] = HouseReviewSerializer(
            reviews_list, many=True
            ).data
        return repr_


    
class CategorySerializer(serializers.ModelSerializer):

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
            "name", 
            "icon",
        )



class HouseLlistSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    totalprice = serializers.IntegerField()
    rating = serializers.FloatField()
    review_count = serializers.SerializerMethodField()
    category = CategorySerializer()
    location = CountriesSerializer()

    class Meta:
        model = House
        fields = (
            "id",
            "category",
            "price",
            "totalprice",
            "image",
            "rating",
            "review_count",
            "discount_interest",
            "name",
            "description",
            "location",
            "people_count",
            "children",
        )

    def get_image(self, obj):
        image = obj.houseimage_set.first()
        return HouseImageSerializer(image).data

    def get_review_count(self, obj):
        count = obj.housereview_set.count()
        return count
    
  

class HouseDetailSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    category = CategorySerializer()
    amenities = serializers.SerializerMethodField()
    hosted_by = serializers.SerializerMethodField()
    location = CountriesSerializer()

    class Meta:
        model = House
        fields = (
            "id",
            "hosted_by",
            "name",
            "living_room",
            "bed_room",
            "bath_room",
            "category",
            "location",
            "address",
            "amenities",
            "discount_interest",
            "description",
            "price",
            "image",
            "people_count",
            "children",
        )

    def get_image(self, obj):
        image = obj.houseimage_set.all()
        return HouseImageSerializer(image, many=True).data

    def get_amenities(self, obj):
        amenities = obj.amenities.all()
        return AdditionalSerializer(amenities, many=True).data
    
    def get_hosted_by(self, obj):
        return f"{obj.hosted_by.name} {obj.hosted_by.surname}"
    

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        repr_["reviews"] = HouseReviewSerializer(
            HouseReview.objects.filter(parent__isnull=True, house=instance), many=True
        ).data
        return repr_
        
        
    
class HouseOrderCreateSerializer(serializers.ModelSerializer):
    house_name = serializers.SerializerMethodField()

    class Meta:
        model = HouseOrder
        fields = (
            "id",
            "name",
            "surname",
            "mobile",
            "email",
            "password_series",
            "house",
            "check_in",
            "check_out",
            "house_name",
        )
        extra_kwargs = {
            "house" : {"write_only":True}
        }

    def get_house_name(self, obj):
        return obj.house.name


class HouseWishlistSerializer(serializers.ModelSerializer):
    house_name = serializers.SerializerMethodField(read_only=True)
    house_category = serializers.SerializerMethodField()
    house_location = serializers.SerializerMethodField()
    house_amenities = serializers.SerializerMethodField()
    house_discount_interest = serializers.SerializerMethodField()
    house_price = serializers.SerializerMethodField()
    house_total_price = serializers.SerializerMethodField()
    house_image = serializers.SerializerMethodField()
    house_bed_room = serializers.SerializerMethodField()
    house_living_room = serializers.SerializerMethodField()
    house_bath_room = serializers.SerializerMethodField()

    class Meta:
        model = Wishlist
        fields = (
            "house",
            "house_id",
            "house_name",
            "house_category",
            "house_location",
            "house_amenities",
            "house_discount_interest",
            "house_price",
            "house_total_price",
            "house_image",
            "house_bed_room",
            "house_living_room",
            "house_bath_room",
        )
        extra_kwargs = {
            "house": {"write_only": True},
        }
    
    def get_house_name(self, obj):
        return obj.house.name
    
    def get_house_category(self, obj):
        return CategorySerializer(obj.house.category).data
    
    def get_house_location(self, obj):
        return CountriesSerializer(obj.house.location).data
    
    def get_house_amenities(self, obj):
        return AdditionalSerializer(obj.house.amenities.all(), many=True).data
    
    def get_house_discount_interest(self, obj):
        return obj.house.discount_interest
    
    def get_house_price(self, obj):
        return obj.house.price
   
    def get_house_total_price(self, obj):
        discount_price = obj.house.price * (obj.house.discount_interest or 0) / 100
        return obj.house.price - discount_price
    
    def get_house_image(self, obj):
        image = HouseImage.objects.filter(house=obj.house)
        return HouseImageSerializer(image, many=True).data
    
    def get_house_bed_room(self, obj):
        return obj.house.bed_room
    
    def get_house_living_room(self, obj):
        return obj.house.living_room
    
    def get_house_bath_room(self, obj):
        return obj.house.bath_room
        
    

class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ("id", "name", "image", "parent")