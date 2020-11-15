from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Cart, CartContain, Product

# Create your views here.
def login_view(request):
    return render(request, "login.html")

def homePage_view(request):
    return render(request, "homepage.html")

@csrf_exempt
def add_cart_product(request):
    pro_id = Product.objects.get(id=request.POST['ID'])
    cart_id = Cart.objects.get(id=1)
    CartContain_obj = CartContain.objects.create(product_id=pro_id, cart_id=cart_id)
    CartContain_obj.save()

    data = {"name" : cart_id.id}
    return JsonResponse(data)

@csrf_exempt
def order_details(request):
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    return JsonResponse(data)

@csrf_exempt
def get_Cart_products(request):
    products = CartContain.objects.filter(cart_id=1)
    data = {"result" : [], "total" : 0}
    sum = 0
    for pro in products:
        pro_id = Product.objects.get(id=pro.product_id.id)
        sum += int(pro_id.price)
        data["result"].append({"name": pro_id.name, "price": pro_id.price})
    data["total"] = sum
    return JsonResponse(data)