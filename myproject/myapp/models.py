from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.user.username
    
    

class MenuItem(models.Model):

    item_name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    storeid=models.CharField(max_length=50,default='default_value')

    def __str__(self):
        return self.item_name
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    paymentmethod = models.CharField(max_length=10, blank=True, null=True)
    paymentbill = models.CharField(max_length=100, blank=True, null=True)
    qrseller  = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return f"Order {self.id} by {self.customer.user.username}"
