from rest_framework import generics, filters
from . .models import House, HouseOrder, HouseReview, Wishlist, Category, Additional
from django.db.models import F, IntegerField
from django.db.models.functions import Coalesce
from django_filters.rest_framework import DjangoFilterBackend
from . filters import HouseFilter
from django.db.models import Avg
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from . .paginations import HousePagination
from . serializers import (
    HouseLlistSerializer, HouseDetailSerializer, HouseOrderCreateSerializer, 
    HouseReviewSerializer, HouseWishlistSerializer, CategoryListSerializer, AdditionalSerializer)



class AdditionalListView(generics.ListAPIView):
    serializer_class = AdditionalSerializer
    queryset = Additional.objects.all()



class HouseListView(generics.ListAPIView):
    serializer_class = HouseLlistSerializer
    pagination_class = HousePagination
    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter
    )
    filterset_class = HouseFilter
    ordering_fields = ("totalprice", "discount_interest", "created_at")

    def get_queryset(self):
        qs = House.objects.annotate(
        disc_interest=Coalesce("discount_interest", 0, output_field=IntegerField()),
        discount_price=F("price") * F("disc_interest") / 100,
        totalprice = F("price") - F("discount_price"),
        rating = Avg("housereview__rating"),
        ).order_by("-created_at")
        return qs



class HouseDetailView(generics.RetrieveAPIView):
    queryset = House.objects.all()
    serializer_class = HouseDetailSerializer
    lookup_field = "id"



class HouseOrderCreateView(generics.CreateAPIView):
    queryset = HouseOrder.objects.all()
    serializer_class = HouseOrderCreateSerializer



class HouseReviewCreateView(generics.CreateAPIView):
    queryset = HouseReview.objects.all()
    serializer_class = HouseReviewSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    


class WishlistView(generics.ListAPIView):
    serializer_class = HouseWishlistSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)
    


class WishlistCreateView(generics.CreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = HouseWishlistSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        house_id = request.data.get("house")
        obj, created = Wishlist.objects.get_or_create(
            user=request.user, house_id=house_id
        )
        if not created:
            obj.delete()
        serializer = self.serializer_class(obj).data
        return Response(serializer)



class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    