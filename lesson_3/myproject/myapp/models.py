from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Clientname: {self.name}, email: {self.email}, ' f'phone_number: {self.phone_number}, address: {self.address}, ' f'registration_date: {self.registration_date}'        

        

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    added_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}'

# class Order(models.Model):
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product)
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     order_date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f'Order #{self.id} by {self.client.name}, Total Amount: {self.total_amount}, Order Date: {self.order_date}'
    


# class OrderManager(models.Model):
    
#     @staticmethod
#     def get_products_in_time_range(orders, start_date):
#         return Product.objects.filter(order__in=orders.filter(order_date__gte=start_date)).distinct()

# class Order(models.Model):
#     objects = OrderManager()

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date = models.DateTimeField()

    def __str__(self):
       return f'Order #{self.id} by {self.client.name}, Total Amount: {self.total_amount}, Order Date: {self.order_date}'