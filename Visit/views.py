from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authentication import SessionAuthentication

from .serializers import *
from rest_framework.permissions import *

class TokenPairView(TokenObtainPairView):
      serializer_class = TokenPairSerializer

class HotelsViewset(viewsets.ModelViewSet):
    queryset = Hotels.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    authentication_classes =JWTAuthentication, SessionAuthentication
    serializer_class = HotelsSerializer


class serviceViewset(viewsets.ModelViewSet):
    queryset = service.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    authentication_classes =JWTAuthentication, SessionAuthentication
    serializer_class = serviceSerializer 


class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    authentication_classes =JWTAuthentication, SessionAuthentication
    serializer_class = CustomerSerializer

class RestaurantViewset(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    authentication_classes =JWTAuthentication, SessionAuthentication
    serializer_class = RestaurantSerializer

class FoodViewset(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    authentication_classes =JWTAuthentication, SessionAuthentication
    serializer_class = FoodSerializer    

class ReservationViewset(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    authentication_classes =JWTAuthentication, SessionAuthentication
    serializer_class = ReservationSerializer


class TouristSiteViewset(viewsets.ModelViewSet):
    queryset = TouristSite.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    authentication_classes =JWTAuthentication, SessionAuthentication
    serializer_class = TouristSiteSerializer 

class barViewset(viewsets.ModelViewSet):
    queryset = bar.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    authentication_classes =JWTAuthentication, SessionAuthentication
    serializer_class = barSerializer

class eventViewset(viewsets.ModelViewSet):
    queryset = event.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    authentication_classes =JWTAuthentication, SessionAuthentication
    serializer_class = eventSerializer  

class lieux_de_loisirsViewset(viewsets.ModelViewSet):
    queryset = event.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    authentication_classes =JWTAuthentication, SessionAuthentication
    serializer_class =lieux_de_loisirsSerializer       



