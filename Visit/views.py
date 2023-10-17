from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authentication import SessionAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .serializers import *
from rest_framework.permissions import *

class TokenPairView(TokenObtainPairView):
      serializer_class = TokenPairSerializer

class HotelsViewset(viewsets.ModelViewSet):
    queryset = Hotels.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    authentication_classes =JWTAuthentication, SessionAuthentication
    serializer_class = HotelsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'adress']
    search_fields = ['name']


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
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'adress']
    search_fields = ['name']

class FoodViewset(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    authentication_classes =JWTAuthentication, SessionAuthentication
    serializer_class = FoodSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'adress']
    search_fields = ['name']    

class ReservationViewset(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    authentication_classes =JWTAuthentication, SessionAuthentication
    serializer_class = ReservationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'adress']
    search_fields = ['name']


class TouristSiteViewset(viewsets.ModelViewSet):
    queryset = TouristSite.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    authentication_classes =JWTAuthentication, SessionAuthentication
    serializer_class = TouristSiteSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'adress']
    search_fields = ['name'] 

class barViewset(viewsets.ModelViewSet):
    queryset = bar.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    authentication_classes =JWTAuthentication, SessionAuthentication
    serializer_class = barSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'adress']
    search_fields = ['name']

class eventViewset(viewsets.ModelViewSet):
    queryset = event.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    authentication_classes =JWTAuthentication, SessionAuthentication
    serializer_class = eventSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'adress']
    search_fields = ['name'] 
    
class lieux_de_loisirsViewset(viewsets.ModelViewSet):
    queryset = lieux_de_loisirs.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    authentication_classes =JWTAuthentication, SessionAuthentication
    serializer_class =lieux_de_loisirsSerializer 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'adress']
    search_fields = ['name']

class ShopViewset(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    authentication_classes =JWTAuthentication, SessionAuthentication
    serializer_class = ShopSerializer 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'adress']
    search_fields = ['name']

class transportViewset(viewsets.ModelViewSet):
    queryset = transport.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    authentication_classes =JWTAuthentication, SessionAuthentication
    serializer_class = transportSerializer 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']      


class HopitalViewset(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    authentication_classes =JWTAuthentication, SessionAuthentication
    serializer_class =HospitalSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'adress']
    search_fields = ['name']       

class ConferenceViewset(viewsets.ModelViewSet):
    queryset =Conference.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    authentication_classes =JWTAuthentication, SessionAuthentication
    serializer_class =ConferenceSerializer 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'adress']
    search_fields = ['name']  

class CultureViewset(viewsets.ModelViewSet):
    queryset = Culture.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    authentication_classes =JWTAuthentication, SessionAuthentication
    serializer_class = CultureSerializer 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'adress']
    search_fields = ['name'] 

class EgliseViewset(viewsets.ModelViewSet):
    queryset = Eglise.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    authentication_classes =JWTAuthentication, SessionAuthentication
    serializer_class = EgliseSerializer   
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'adress']
    search_fields = ['name']  
    




