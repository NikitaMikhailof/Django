from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telephone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, telephone: {self.telephone}'
    

class Product(models.Model):
    name = models.CharField(max_length=50)
    discription = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f'Product: {self.name}, discription: {self.discription}, price: {self.price}'
    

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Customer_order:  {self.customer.name}, quantity: {self.quantity}, total price:  {self.total_price}, date_ordered: {self.date_ordered}'
    
