from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    quantity_choices = [
        ('GM' , 'Gram'),
        ('LT' , 'Litre'),
        ('UNIT' , 'Units')
    ]
    product_name = models.CharField(max_length=100)
    product_quantity_type = models.CharField(max_length=10 , choices=quantity_choices , default=quantity_choices[2][0])
    product_price = models.IntegerField()
    produc_quantity_in_inventory = models.IntegerField(null=True, blank=True)
    product_category = models.ForeignKey(Categories, related_name='product' , on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.product_name 


class Employee(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    adhaar = models.CharField(max_length=12)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50 , null=True , blank=True)
    address = models.CharField(max_length=200)
   
    def __str__(self):
        return self.name


class Orders(models.Model):
    order_id = models.IntegerField()
    order_created = models.DateTimeField()
    products = models.ManyToManyField(Product)
    total_order_price = models.IntegerField()
    customer_ordered = models.ForeignKey(Customer, related_name='customer_order', on_delete=models.DO_NOTHING , null=True)
    employee = models.ForeignKey(Employee , related_name='order_handler', on_delete=models.DO_NOTHING , null=True)
    def __str__(self):
        return f"{self.order_id} - {self.total_order_price}"

