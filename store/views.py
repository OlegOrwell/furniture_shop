from django.shortcuts import get_object_or_404, render

from .models import Category, Products

# Create your views here.
def products_all(request):
    products = Products.products.all()
    return render(request, 'store/home.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Products, slug=slug, in_stock=True)
    return render(request, 'store/products/product.html', {'product': product})

def category_list(request, search_slug=None):
    category = get_object_or_404(Category, slug=search_slug)
    products = Products.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})
