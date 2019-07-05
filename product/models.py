from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    """
    Category Model
    column: name, description, slug
    """
    name = models.CharField(max_length=250)
    decription = models.TextField()
    slug = models.SlugField(max_length=250, unique=True)
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name
class Address(models.Model):
    house_no = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    village = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pincode = models.IntegerField()
    def __str__(self):
        return "{}, {}, {}, {}, {}, {}".format(self.house_no,self.street,self.village, self.state,self.pincode,self.country)

class Farmer(models.Model):
    basic_detail = models.OneToOneField(User,on_delete=models.CASCADE)
    Address = models.OneToOneField(Address, on_delete=models.CASCADE)
    def __str__(self):
        return self.basic_detail.username
class Product(models.Model):
    """
    Category Product
    column: name, description, slug, updated, price, cultivation_date
    """
    name = models.CharField(max_length=250)
    decription = models.TextField()
    slug = models.SlugField(max_length=250, unique=True)
    updated = models.DateTimeField(auto_now='True')
    price = models.DecimalField(decimal_places=2,max_digits=10)
    cultivation_date = models.DateTimeField()
    originated_from = models.ForeignKey(Farmer, on_delete=models.CASCADE,related_name='products')
    class Meta:
        ordering = ['-updated']
    def __str__(self):
        return self.name
class ProductImages(models.Model):
    PRIORITY = [(i,str(i)) for i in range(1,10)]
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='product/images/%y/%m/%d')
    priority = models.IntegerField(choices=PRIORITY)
    class Meta:
        ordering = ['priority']
    def __str__(self):
        return self.product.name
