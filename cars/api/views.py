from rest_framework import generics, filters
from . .models import Car, CarOrder, CarReview, Wishlist
from django.db.models import F, IntegerField
from django.db.models.functions import Coalesce
from django_filters.rest_framework import DjangoFilterBackend
from . filters import CarFilter
from django.db.models import Avg
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..paginations import CarPagination
from . serializers import (
    CarListSerializer, CarDetailSerializer, CarOrderSerializer,
    CarReviewSerializer, CarWishlistSerializer)



class CarListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    pagination_class = CarPagination
    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter
    )
    filterset_class = CarFilter
    ordering_fields = ("totalprice", "discount_interest", "rent_per_day")

    def get_queryset (self):
        qs = Car.objects.annotate(
        dic_interest=Coalesce("discount_interest", 0, output_field=IntegerField()),
        discount_price=F("rent_per_day") * F("dic_interest") / 100,
        totalprice=F("rent_per_day") - F("discount_price"),
        rating = Avg("carreview__rating")
        ).order_by("-created_at")
        return qs

       
    
class CarDetailView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarDetailSerializer
    lookup_field = "id"



class CarOrderCreateView(generics.CreateAPIView):
    queryset = CarOrder.objects.all()
    serializer_class = CarOrderSerializer



class CarReviewCreateView(generics.CreateAPIView):
    queryset = CarReview.objects.all()
    serializer_class = CarReviewSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    


class WishlistView(generics.ListAPIView):
    serializer_class = CarWishlistSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)
    


class WishlistCreateView(generics.CreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = CarWishlistSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        car_id = request.data.get("car")
        obj, created = Wishlist.objects.get_or_create(
            user=request.user, car_id=car_id
        )
        if not created:
            obj.delete()
        serializer = self.serializer_class(obj).data
        return Response(serializer)

  
  
    

  