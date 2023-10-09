from django.db import models
from accounts.models import CustomUser
# Create your models here.

class Prand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(CustomUser, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
    @property
    def ImageUrl(self):
        try:
            return self.image.url
        except:
            url = ''
        return url
    
class Properties(models.Model):
    product = models.OneToOneField(Product, related_name='properties_product', on_delete=models.CASCADE, null=True)
    company = models.ForeignKey(Prand, related_name='prand_properties', on_delete=models.CASCADE)
    color = models.CharField(max_length=100)
    generation = models.IntegerField()
    processor = models.CharField(max_length=200)
    instelled_RAM = models.CharField(max_length=10)
    System_type = models.CharField(max_length=50)
    storege = models.CharField(max_length=50)
    graphics_card = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.id)
    
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transcation_id = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_total_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
    @property
    def shipping(self):
        shipping = False
        orderItems = self.orderitem_set.all()
        for orderItem in orderItems:
            if orderItem.product.digital == False:
                shipping = True
        return shipping
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.id)
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city =models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    zipcode =models.CharField(max_length=200, null=True, blank=True)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
    