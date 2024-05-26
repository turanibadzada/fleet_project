from rest_framework import generics, filters
from . serializers import TicketSalesListSerializer, TicketOrderCreateSerializer, TicketDetailSerializer, WishlistSerializer
from . .models import TicketSales, TicketOrder, Wishlist
from django_filters.rest_framework import DjangoFilterBackend
from . filters import TicketFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from . serializers import (
    TicketSalesListSerializer, TicketOrderCreateSerializer, 
    TicketDetailSerializer, WishlistSerializer)



class TicketSalesListView(generics.ListAPIView):
    queryset = TicketSales.objects.all()
    serializer_class = TicketSalesListSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter
    )
    filterset_class = TicketFilter
    ordering_fields = ("price", "departure_time", "arrivel_time", "parking_areas")



class TicketDetailView(generics.RetrieveAPIView):
    queryset = TicketSales.objects.all()
    serializer_class = TicketDetailSerializer
    lookup_field = "id"



class TicketOrderCreateSerializer(generics.CreateAPIView):
    queryset = TicketOrder.objects.all()
    serializer_class = TicketOrderCreateSerializer



class WishlistView(generics.ListAPIView):
    serializer_class = WishlistSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)
    


class WishlistCreateView(generics.CreateAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        ticketsales_id = request.data.get("ticketsales")
        obj, created = Wishlist.objects.get_or_create(
            user=request.user, ticketsales_id=ticketsales_id
        )
        if not created:
            obj.delete()
        serializer = self.serializer_class(obj).data
        return Response(serializer)

