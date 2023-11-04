from django.shortcuts import render, redirect
import socket
from cart.models import Cart


def cartPage(request):
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    cart = Cart.objects.get(ip=ip)
    products = cart.cartItems.all()
    data = {"cart": cart, "products": products}
    return render(request, "cart.html", data)


def addCart(request):
    if request.method == "POST":
        productId = request.POST.get("productId")
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        try:
            cart = Cart.objects.get(ip=ip)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(ip=ip, total=0, shipping=0, cartTotal=0)
        cart = Cart.add_or_update_cart(productId, ip)
    return redirect("/cart")
