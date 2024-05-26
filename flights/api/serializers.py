from rest_framework import serializers
from . .models import Company, TicketSales, TicketOrder, Wishlist, Countries

class CountriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Countries
        fields = (
            "name", 
            "image",
        )



class CompanySerializer(serializers.ModelSerializer):
    company_location = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = (
            "name", 
            "description", 
            "company_location", 
            "image",
        )

    def get_company_location(self, obj):
        return obj.company_location.name



class TicketSalesListSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    departure_country = serializers.SerializerMethodField()
    destination_country = serializers.SerializerMethodField()

    class Meta:
        model = TicketSales
        fields = (
            "description",
            "departure_country",
            "destination_country",
            "departure_time",
            "arrivel_time",
            "company",
            "departure_country",
            "destination_country",
            "price",
            "people_count",
            "children_count",
        )
          
    def get_departure_country(self, obj):
        return obj.departure_country.name
    
    def get_destination_country(self, obj):
        return obj.destination_country.name



class TicketDetailSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    departure_country = serializers.SerializerMethodField()
    destination_country = serializers.SerializerMethodField()

    class Meta:
        model = TicketSales
        fields = (
            "id",
            "description",
            "departure_time",
            "arrivel_time",
            "price",
            "departure_country",
            "destination_country",
            "company",
            "parking_areas",
            "class_of_services",
            "people_count",
            "children_count",
        )

    def get_departure_country(self, obj):
        return obj.departure_country.name

    def get_destination_country(self, obj):
        return obj.destination_country.name
    


class TicketOrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TicketOrder
        fields = (
            "name",
            "surname",
            "mobile",
            "email",
            "password_series",
            "ticket_sales",
        )



class WishlistSerializer(serializers.ModelSerializer):
    ticketsales_departure_time = serializers.SerializerMethodField()
    ticketsales_arrivel_time = serializers.SerializerMethodField()
    ticketsales_price = serializers.SerializerMethodField()
    ticketsales_departure_country = serializers.SerializerMethodField()
    ticketsales_destination_country = serializers.SerializerMethodField()
    ticketsales_company = serializers.SerializerMethodField()
    ticketsales_parking_areas = serializers.SerializerMethodField()
    ticketsales_class_of_services = serializers.SerializerMethodField()
    ticketsales_people_count = serializers.SerializerMethodField()
    ticketsales_children_count = serializers.SerializerMethodField()

    class Meta:
        model = Wishlist
        fields = (
            "ticketsales",
            "ticketsales_id",
            "ticketsales_departure_time",
            "ticketsales_arrivel_time",
            "ticketsales_price",
            "ticketsales_departure_country",
            "ticketsales_destination_country",
            "ticketsales_company",
            "ticketsales_parking_areas",
            "ticketsales_class_of_services",
            "ticketsales_people_count",
            "ticketsales_children_count",
        )
        extra_kwargs = {
            "ticketsales": {"write_only": True},
        }


    def get_ticketsales_departure_time(self, obj):
        return obj.ticketsales.departure_time
    
    def get_ticketsales_arrivel_time(self, obj):
        return obj.ticketsales.arrivel_time
    
    def get_ticketsales_price(self, obj):
        return obj.ticketsales.price
    
    def get_ticketsales_departure_country(self, obj):
        return CountriesSerializer(obj.ticketsales.departure_country).data
    
    def get_ticketsales_destination_country(self, obj):
        return CountriesSerializer(obj.ticketsales.destination_country).data
    
    def get_ticketsales_company(self, obj):
        return CompanySerializer(obj.ticketsales.company).data
    
    def get_ticketsales_parking_areas(self, obj):
        return obj.ticketsales.parking_areas
    
    def get_ticketsales_class_of_services(self, obj):
        return obj.ticketsales.class_of_services
    
    def get_ticketsales_people_count(self, obj):
        return obj.ticketsales.people_count
    
    def get_ticketsales_children_count(self, obj):
        return obj.ticketsales.children_count

    
    