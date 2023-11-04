from django.db import models
from products.models import Product


class Cart(models.Model):
    total = models.IntegerField()
    ip = models.CharField(max_length=100)
    shipping = models.IntegerField()
    cartTotal = models.IntegerField()
    cartItems = models.ManyToManyField(Product)

    def __str__(self):
        return f"Cart {self.id}"

    @classmethod
    def add_or_update_cart(self, product_id, ip_address):
        try:
            cart = self.objects.get(ip=ip_address)
        except self.DoesNotExist:
            cart = self.objects.create(ip=ip_address, total=0, shipping=0, cartTotal=0)

        product = Product.objects.get(pk=product_id)
        cart.cartItems.add(product)

        # Update total, shipping, cartTotal based on the added product
        cart.update_cart_totals()
        return cart

    def update_cart_totals(self):
        self.total = sum(item.price for item in self.cartItems.all())
        self.shipping = 10  # example shipping cost
        self.cartTotal = self.total + self.shipping
        self.save()
