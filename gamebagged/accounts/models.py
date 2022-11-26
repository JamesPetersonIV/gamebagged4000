from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#represent database tables

#user 
#class Customer(models.Model):
    #customer = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)

#class Bagger(models.Model):
    #bagger = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)

#category
#class Category(models.Model):
    #name 
    #db_index~
    #name = models.CharField(max_length=255, db_index=True, null=True)
    #unique~ on one can have the name
    #slug = models.SlugField(max_length=2555, unique=True, null=True)

    #instructions
    #class Meta:
        #database name
        #verbose_name_plural = 'categories'
        #ordering categories
        #ordering = ('name',)
    #default 'name' returned
    #def __str__(self):
        #return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)    

    def __str__(self):
        return self.name    
        
#product
class Product(models.Model):
    #category
    CATEGORY = (
        ('Video Games', 'Video Games'),
        ('Accessories', 'Accessories'),
        ('Mobile Phones', 'Mobile Phones'),
        ('Consoles', 'Consoles'),
    ) 

    #title of product
    name = models.CharField(max_length=100, null=True)
    #text form of data
    description = models.TextField()
    #picture of item
    img = models.ImageField(upload_to='images/', null=True)
    #present individual item on page
    slug = models.SlugField(max_length=255, null= True)
    #price of item
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    #will be able to select from contents in CATEGORY
    category = models.CharField(max_length=200, default=False,blank=True, choices=CATEGORY)
    tags = models.ManyToManyField(Tag)


    class Meta:
        ordering = ('name',)

    #default 'name' returned
    def __str__(self):
        return self.name


class OrderPro(models.Model):
    #connected to status/tuples
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    items = models.ManyToManyField(Product, verbose_name='product', blank=True)
    #will be able to select from contents in STATUS
    status = models.CharField(max_length=200, default='Pending', blank=True , choices=STATUS)
    customer = models.ForeignKey(User, verbose_name='customer', null = True, on_delete=models.SET_NULL)
    bagger = models.OneToOneField(User, null=True, related_name='bagger', on_delete=models.SET_NULL)
    
    class Meta:
        ordering = ('created_on',)



#user pk >> profile 
#profile fk >> customer pk/ profile fk >> bagger
