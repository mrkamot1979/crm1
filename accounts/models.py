from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50, null=True) #null=True essentially makes it OK to not set a default value
    phone = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=50, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + "  " + self.phone

class Product(models.Model):
    CATEGORY = (
                    ('Indoor', 'Indoor'),
                    ('Outdoor', 'Outdoor'),
    )

    name = models.CharField(max_length=50, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True) #null=True essentially makes it OK to not set a default value

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
                ('Pending', 'Pending'),
                ('Out for delivery', 'Out for delivery'),
                ('Delivered', 'Delivered')
    )

    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)
    tags = models.ManyToManyField(Tag)

