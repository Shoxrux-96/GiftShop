from django.db import models
import datetime
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=150)
    soni = models.CharField(max_length=15)
    image = models.ImageField(upload_to='category_images/', default='category_image.jpg')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'categories'
    
class Product(models.Model):
    
    class Status(models.TextChoices):
        Active = 'AC','Active',
        Noactive = 'NO', 'Noactive',
    
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/media')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=255)
    date = models.DateField(default=datetime.datetime.today)
    discount = models.FloatField(blank=True, null=True)
    size = models.CharField(max_length=150)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.Noactive)
    
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=13, null=False)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}' 
            
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=150)
    color = models.CharField(max_length=1, choices=(('B','Black'),('W','White'), ('R','Red'),('B','Blue'), ('G','Green')))
    address = models.CharField(max_length=100, default="", blank=True)
    phone = models.CharField(max_length=13, default="" , blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.product
    

class mashxur(models.Model):
    nomi = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/mashxur')
    chegirma = models.CharField(max_length=30)

    def __str__(self):
        return self.nomi