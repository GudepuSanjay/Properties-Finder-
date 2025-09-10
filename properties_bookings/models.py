from django.db import models
from django.conf import settings
from properties.models import Property
# Create your models here.
class Bookings(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    property=models.ForeignKey(Property,on_delete=models.CASCADE)
    visit_date=models.DateField()
    message=models.TextField(blank=True,null=True)
    status=models.CharField(max_length=20,choices=[('Pending','Pending'),('Confirmed','Confirmed'),('Cancelled','Cancelled')],default='Pending')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.property.title} ({self.status})"