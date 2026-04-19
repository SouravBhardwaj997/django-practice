from django.contrib import admin

# Register your models here.

from .models import Product,ProductReview,Stores

admin.site.register(Product)
admin.site.register(ProductReview)
admin.site.register(Stores)