from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse, redirect
from products.models import Category


@csrf_exempt
def homepage(request):
    categories = Category.objects.all()
    data = {"categories": categories}
    return render(request, "homepage.html", data)
