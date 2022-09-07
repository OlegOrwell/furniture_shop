from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .cart import Cart
from store.models import Products

from decimal import Decimal

# Create your views here.
def cart_summary(request):
    cart = Cart(request)
    return render(request, 'cart/summary.html')

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == "post":
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Products, id=product_id)
        cart.add(product=product, qty=product_qty)
        price_current = cart.price_current(product)
        price_total = cart.get_total()
        response = JsonResponse({'qty': cart.__len__(), 'price': price_current, 'price_total': price_total})
        return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == "delete":
        product_id = int(request.POST.get('productid'))
        cart.delete(product_id=product_id)
    response = JsonResponse({'qty': cart.__len__()})
    return response