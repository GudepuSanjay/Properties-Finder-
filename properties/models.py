from decimal import Decimal
from django.db import models
from django.conf import settings
from multiselectfield import MultiSelectField
# Create your models here.
class Property(models.Model):
    PROPERTY_CHOICES=[
        ('Flat','Flat'),
        ('Villa','Villa'),
        ('Plot','Plot'),
        ('Commercial','Commercial')
    ]

    STATUS_CHOICES=[
        ('Available','Available'),
        ('Sold','Sold'),
        ('Rented','Rented')
    ]

    AMENITIES=[
        ('Parking','Parking'),
        ('SwimmingPool','SwimmingPool'),
        ('AirConditioning','AirConditioning'),
        ('Gym','Gym')
    ]

    TYPE_PROPERTY=[
        ('Rent','Rent'),
        ('Sale','Sale'),
        ('Lease','Lease')
    ]
    
    agent=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name="properties")
    title=models.CharField(max_length=200)
    description=models.TextField()
    price=models.DecimalField(max_digits=12,decimal_places=2)
    property_type=models.CharField(max_length=20,choices=PROPERTY_CHOICES)
    amenities=MultiSelectField(choices=AMENITIES,default=['Parking'])
    bathrooms = models.IntegerField(default=1)
    bedrooms = models.IntegerField(default=1)
    squarefeets=models.DecimalField(max_digits=20,decimal_places=3,default=Decimal(100.000))
    type_property=models.CharField(max_length=100,choices=TYPE_PROPERTY,default="Rent")
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default="Available")
    image=models.ImageField(upload_to='property_images/')
    locations=models.CharField(max_length=200)
    zip_code=models.IntegerField(default=1234)
    near_location = models.CharField(max_length=1000,default="Near Location")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title