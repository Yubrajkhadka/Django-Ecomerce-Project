from django.db import models
from django.contrib.auth.models import User



class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='admin')
    full_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length =100 , unique =True)
    slug = models.SlugField(max_length =100, unique = True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)    
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField(default=1)
   
    def __str__(self):
        return self.name



class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    number = models.CharField(default=False,max_length=10)
    message = models.TextField()
    def __str__(self):
        return self.name



ORDER_STATUS = (
    ("Order Received", "Order Received"),
    ("Order Processing", "Order Processing"),
    ("On the way", "On the way"),
    ("Order Completed", "Order Completed"),
    ("Order Cancelled", "Order Cancelled"),
)

METHOD = (
    ("Cash On Delivery", "Cash On Delivery"),
    ("Khalti", "Khalti"),
   
)

    

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length =10)
    email = models.EmailField(max_length=60)
    additional_info = models.TextField()
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS,default="Order Received")
    payment_method = models.CharField(
        max_length=20, choices=METHOD, default="Cash On Delivery")
    paid = models.BooleanField(default=False,null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product = models.CharField(max_length=255)
    image = models.ImageField(upload_to ='order/photos')
    quantity = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    total = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.order.user.username
    

    

    

