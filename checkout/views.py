import socket
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse, redirect
from cart.models import Cart
from products.models import Category


@csrf_exempt
def checkout(request):
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    cart = Cart.objects.get(ip=ip)
    products = cart.cartItems.all()
    data = {"cart": cart, "products": products}
    return render(request, "checkout.html", data)
