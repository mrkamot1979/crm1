from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50, null=True) #null=True essentially makes it OK to not set a default value
    phone = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=50, null=True)
    date_created = models.DateTimeField(auto_now_add=True)


