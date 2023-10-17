from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class TokenPairSerializer(TokenObtainPairSerializer):
      def validate(self, attrs):
         data = super(TokenPairSerializer, self).validate(attrs)
         data['groups'] = [group.name for group in self.user.groups.all()]
         data ['username'] = self.user.username
         data ['id'] = self.user.id
         data ['first_name_'] = self.user.first_name
         data ['last_name'] = self.user.last_name
         return data


class HotelsSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
         data = super().to_representation(instance)
         data["service_name"] = instance.service.name
         data["service_price"] = instance.produit.price
         return data
    
    
    class Meta:
         model = Hotels
         fields = "__all__"



class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
         model = Restaurant
         fields = "__all__" 

class serviceSerializer(serializers.ModelSerializer):
    class Meta:
         model = service
         fields = "__all__" 


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
         model = Food
         fields = "__all__" 


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
         model = Reservation
         fields = "__all__"  
              
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
         model = Customer
         fields = "__all__"        
class TouristSiteSerializer(serializers.ModelSerializer):
    class Meta:
         model = TouristSite
         fields = "__all__"  

class barSerializer(serializers.ModelSerializer):
    class Meta:
         model = bar
         fields = "__all__"  
     

class eventSerializer(serializers.ModelSerializer):
    class Meta:
         model = event
         fields = "__all__"  


class lieux_de_loisirsSerializer(serializers.ModelSerializer):
    class Meta:
         model = lieux_de_loisirs
         fields = "__all__"     


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
         model = Shop
         fields = "__all__"   
         
class transportSerializer(serializers.ModelSerializer):
    class Meta:
         model = transport
         fields = "__all__" 

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
         model = Hospital
         fields = "__all__"   

class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
         model = Conference
         fields = "__all__" 

class CultureSerializer(serializers.ModelSerializer):
    class Meta:
         model = Culture
         fields = "__all__"  

class EgliseSerializer(serializers.ModelSerializer):
    class Meta:
         model = Eglise
         fields = "__all__"              



            
