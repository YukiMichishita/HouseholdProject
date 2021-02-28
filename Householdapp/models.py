from django.db import models

# Create your models here.


#class Grocery(models.Model):
#    name = models.CharField(max_length=100)
#
#
#class Unit(models.Model):
#    name = models.CharField(max_length=50)
#
#
#class Refrigerator(models.Model):
#    grocery = models.ForeignKey('Grocery', on_delete=models.CASCADE)
#    unit = models.ForeignKey('Unit', on_delete=models.PROTECT)
#    quantity = models.IntegerField(max_length=10)
#    purchase_date = models.DateField(auto_now_add=True)
#
#
#class Category(models.Model):
#    category_name = models.CharField(max_length=50)
#
#
#class Housekeeping_Book(models.Model):
#    category = models.ForeignKey('Category', on_delete=models.CASCADE)
#    price = models.IntegerField(max_length=10)
#    quantity = models.IntegerField(max_length=10)
#    purchase_date = models.DateField(auto_now_add=True)
