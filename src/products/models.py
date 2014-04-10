from django.db import models

from categories.models import Category
from suppliers.models import Supplier

class Product(models.Model):
    productname = models.CharField(db_column='ProductName', max_length=40) # Field name made lowercase.
    supplier = models.ForeignKey(Supplier)
    category = models.ForeignKey(Category)
    quantityperunit = models.CharField(db_column='QuantityPerUnit', max_length=20, blank=True) # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True) # Field name made lowercase.
    unitsinstock = models.CharField(db_column='UnitsInStock', blank=True, null=True, max_length=20,) # Field name made lowercase.
    unitsonorder = models.SmallIntegerField(db_column='UnitsOnOrder', blank=True, null=True) # Field name made lowercase.
    reorderlevel = models.SmallIntegerField(db_column='ReorderLevel', blank=True, null=True) # Field name made lowercase.
    discontinued = models.IntegerField(db_column='Discontinued') # Field name made lowercase.
    class Meta:
        db_table = 'products'
