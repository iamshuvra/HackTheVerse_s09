from django.db import models

# Create your models here.
class Product(models.Model):
    name    = models.CharField(max_length=30)
    price   = models.CharField(max_length=30)

class Customer(models.Model):
    full_name   =   models.CharField(max_length=30)
    email       =   models.EmailField(max_length=20)
    password    =   models.CharField(max_length=30)
    username    =   models.CharField(max_length=20)

class Order(models.Model):
    total_amount =  models.DecimalField(max_digits=19, decimal_places=2)
    date        =   models.DateField(auto_now_add=True)
    cus_id      =   models.ForeignKey(Customer, on_delete=models.CASCADE)

class Include(models.Model):
    order_id    =   models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id  =   models.ForeignKey(Product, on_delete=models.CASCADE)

class Cart(models.Model):
    noOfProducts  =   models.IntegerField()

class CartContain(models.Model):
    product_id  =   models.ForeignKey(Product, on_delete=models.CASCADE)
    cart_id     =   models.ForeignKey(Cart, on_delete=models.CASCADE)