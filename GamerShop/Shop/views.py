from django.shortcuts import render
from .models import *


def home(request):
    prods = Products.objects.all()[:2]
    product_carusel = Products.objects.all()[2:5]
    return render(request, 'index.html', {'products': prods, 'prod_carusel': product_carusel}, )


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def product(request):
    prod = Products.objects.all()
    return render(request, 'product.html', {"prod": prod})


def remot(request):
    return render(request, 'remot.html')


def video(request):
    return render(request, 'video.html')


def product_detail(request, id):
    product = Products.objects.get(id=id)
    return render(request, 'product_detail.html', {'product': product})