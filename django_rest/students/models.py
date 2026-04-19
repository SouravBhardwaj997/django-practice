from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    price=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.name}'

class ProductReview(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    review=models.TextField()
    reviewer=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.product.name} reviewed by {self.reviewer.first_name}'


class Stores(models.Model):
    name=models.CharField(max_length=20)
    location=models.CharField(max_length=10)
    products=models.ManyToManyField(Product,related_name="stores")
    def __str__(self):
        return f"{self.name}"
    
class ProductCertificate(models.Model):
    certificate_no=models.CharField(max_length=10)
    product=models.OneToOneField(Product,on_delete=models.CASCADE,related_name="certificate")   