from django.shortcuts import render
from .models import *
def home(request):
    ctg = Category.objects.all()
    product = Product.objects.all()
    ctx={'ctg': ctg, 'product': product}
    return render(request, 'index.html', ctx)
def contact(request):
    ctx = {}
    return render(request, 'contact.html', ctx)
def products(request, slug = None):
    ctg = Category.objects.all()
    category = Category.objects.get(slug = slug)
    product = Product.objects.all().filter(type_id = category.id)
    ctx = {'ctg': ctg, 'category': category, 'product': product}
    return render(request, 'products.html', ctx)
def register(request):
    ctx = {}
    return render(request, 'register.html', ctx)
def single(request):
    ctx = {}
    return render(request, 'single.html', ctx)