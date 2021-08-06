from django.db import models
from django.contrib.auth.models import User
from apps.products.models import Product


# Create your models here.
class Cart(models.Model):
    cart_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product)

    class Meta:
        ordering = ['cart_id', '-created_at']

    def __str__(self):
        return f'{self.cart_id}'
