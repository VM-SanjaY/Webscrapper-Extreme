from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=300,blank=True,null=True)
    modelname = models.CharField(max_length=300,blank=True,null=True)

class Electronicinfo(models.Model):
    usersearch = models.CharField(max_length=300,blank=True,null=True)
    brandname = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True,blank=True)
    productname = models.CharField(max_length=300,blank=True,null=True)
    rating = models.CharField(max_length=30,null=True,blank=True)
    image = models.ImageField(null=True,blank=True, max_length=3000)
    price = models.CharField(max_length=30,blank=True,null=True)
    site = models.CharField(max_length=300,blank=True,null=True)
    siteurl = models.CharField(max_length=3000,blank=True,null=True)
    imageurl = models.ImageField(max_length=3000, blank=True, null=True)











