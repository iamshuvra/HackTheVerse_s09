from django.contrib import admin
from .models import Product, Order, Customer, Include, Cart, CartContain
# Register your models here.
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Include)
admin.site.register(Cart)
admin.site.register(CartContain)