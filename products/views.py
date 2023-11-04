from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse
from .models import Product, Category
from django.contrib.staticfiles.views import serve
from django.conf import settings
import json


@csrf_protect
def addProduct(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        image = request.FILES.get("image")
        category_ids = request.POST.getlist("category")
        new_product = Product(
            name=name,
            description=description,
            price=price,
            image=image,
        )
        new_product.save()
        for category_id in category_ids:
            category = Category.objects.get(pk=category_id)
            new_product.category.add(category)
        return redirect("/products")
    else:
        categories = Category.objects.all()
        data = {"categories": categories}

        return render(request, "addProduct.html", data)


@csrf_exempt
def addCategory(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        new_category = Category(name=name, description=description)
        new_category.save()
        return redirect("/products/add/")
    else:
        return render(request, "addCategory.html")


@csrf_exempt
def viewProducts(request):
    category = request.GET.get("category")
    categories = Category.objects.all()

    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    print(Product.objects.filter(category=7)[0].category)

    data = {"products": products, "categories": categories, "category_name": category}
    return render(request, "products.html", data)


@csrf_exempt
def viewProduct(request):
    id = request.GET.get("id")
    product = Product.objects.get(pk=int(id))
    catogries = product.category.all()

    data = {"product": product, "category": catogries.first}
    return render(request, "product_page.html", data)
