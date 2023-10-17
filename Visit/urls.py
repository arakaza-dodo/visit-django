
from django.urls import path, include
from rest_framework import routers
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

router = routers.DefaultRouter()
router.register("hotel", HotelsViewset)
router.register("customer", CustomerViewset)
router.register("service", serviceViewset)
router.register("restaurant", RestaurantViewset)
router.register("food", FoodViewset)
router.register("reservation", ReservationViewset)
router.register("TouristSite", TouristSiteViewset)
router.register("bar", barViewset)
router.register("lieux_de_loisirs", lieux_de_loisirsViewset)  
router.register("Shop", ShopViewset)
router.register("transport", transportViewset)    
router.register("Hopital", HopitalViewset)  
router.register("Conference", ConferenceViewset)  
router.register("culture", CultureViewset)  
router.register("Eglise", EgliseViewset)  
          



urlpatterns = [
    path('', include(router.urls)),
    path('login/',TokenPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('api-auth/',include('rest_framework.urls')),
]
