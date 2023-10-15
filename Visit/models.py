
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='service_photos/')

    def __str__(self):
        return self.name

class Hotels(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    room_types = models.CharField(max_length=200)  
    service = models.ForeignKey(service, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='hotels_photos/')
    stars = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nom
    


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"   

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    capacity = models.IntegerField()
    service = models.ForeignKey(service, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='restaurant_photos/')
    is_available = models.BooleanField(default=True)
    

    def __str__(self):
        return self.name
    

class Food(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='food_photos/')
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.nom  


class Reservation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    service  = models.ForeignKey(service, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    

    def __str__(self):
        return f"{self.customer.username} - {self.service} - {self.date} - {self.time}"
    
    
class TouristSite(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='sites_touristiques_photos/')
    open_time = models.DateTimeField()
    close_time = models.DateTimeField()

class bar(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    stars = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='bar_photos/')
    boissons = models.CharField(max_length=100)
    service = models.ForeignKey(service, on_delete=models.CASCADE)
  

    def str(self):
        return self.name 
     
class event(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='event_photos/')
    open_time = models.DateTimeField()
    close_time = models.DateTimeField()

    def str(self):
        return self.name 
     
class lieux_de_loisirs(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='lieux_de_loisirs_photos/')
    open_time = models.DateTimeField()
    close_time = models.DateTimeField()

    def str(self):
        return self.name 


class Shop(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    # state = models.CharField(max_length=2)
    # zip_code = models.CharField(max_length=10)  


class Hospital(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    # state = models.CharField(max_length=2)
    # zip_code = models.CharField(max_length=10)
    # myapp/models.py

class Province(models.Model):
    name = models.CharField(max_length=255)

class quartier(models.Model):
    name = models.CharField(max_length=255)



class Role(models.Model):
    user = models.ForeignKey(User,on_delete=models.PROTECT)
    nom = models.CharField(max_length=100)   




    
