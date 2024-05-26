from rest_framework import generics, filters
from ..models import News, Event, EventOrder, Wishlist
from django.db.models import F, IntegerField
from django.db.models.functions import Coalesce
from django.db.models import Avg
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from . filters import EventFilter
from .serializers import (
    NewsListSerializer, NewsDetailSerializer, EventListSerializer, 
    EventDetailSerializer, EventReviewSerializer, EventOrderCreateSerializer, EventWishlistSerializer)



class NewsListView(generics.ListAPIView):
    serializer_class = NewsListSerializer
    queryset = News.objects.all()



class NewsDetailView(generics.RetrieveAPIView):
    serializer_class = NewsDetailSerializer
    queryset = News.objects.all()
    lookup_field = "id"



class EventListView(generics.ListAPIView):
    serializer_class = EventListSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter
    )
    filterset_class = EventFilter
    ordering_fields = ("start_date", "end_date")
    
    def get_queryset(self):
        qs = Event.objects.annotate(
        disc_interest=Coalesce("discount_price", 0, output_field=IntegerField()),
        disc_price=F("price") * F("disc_interest") / 100,
        totalprice = F("price") - F("disc_price"),
        rating = Avg("eventreview__rating")
        ).order_by("-created_at")
        return qs



class EventDetailView(generics.RetrieveAPIView):
    serializer_class = EventDetailSerializer
    queryset = Event.objects.all()
    lookup_field = "id"



class EventReviewCreateView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventReviewSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    


class EventOrderCreateView(generics.CreateAPIView):
    queryset = EventOrder.objects.all()
    serializer_class = EventOrderCreateSerializer



class WishlistView(generics.ListAPIView):
    serializer_class = EventWishlistSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)
    


class WishlistCreateView(generics.CreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = EventWishlistSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        event_id = request.data.get("event")
        obj, created = Wishlist.objects.get_or_create(
            user=request.user, event_id=event_id
        )
        if not created:
            obj.delete()
        serializer = self.serializer_class(obj).data
        return Response(serializer)