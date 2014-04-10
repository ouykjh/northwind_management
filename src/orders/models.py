from django.db import models

from customers.models import Customer
from employees.models import Employee

class Order(models.Model):
    customer = models.ForeignKey(Customer)
    employee = models.ForeignKey(Employee)
    orderdate = models.DateField(db_column='OrderDate', blank=True, null=True) # Field name made lowercase.
    requireddate = models.DateField(db_column='RequiredDate', blank=True, null=True) # Field name made lowercase.
    shippeddate = models.DateField(db_column='ShippedDate', blank=True, null=True) # Field name made lowercase.
    shipvia = models.SmallIntegerField(db_column='ShipVia', blank=True, null=True) # Field name made lowercase.
    freight = models.FloatField(db_column='Freight', blank=True, null=True) # Field name made lowercase.
    shipname = models.CharField(db_column='ShipName', max_length=40, blank=True, null=True) # Field name made lowercase.
    shipaddress = models.CharField(db_column='ShipAddress', max_length=60, blank=True, null=True) # Field name made lowercase.
    shipcity = models.CharField(db_column='ShipCity', max_length=15, blank=True, null=True) # Field name made lowercase.
    shipregion = models.CharField(db_column='ShipRegion', max_length=15, blank=True, null=True) # Field name made lowercase.
    shippostalcode = models.CharField(db_column='ShipPostalCode', max_length=10, blank=True, null=True) # Field name made lowercase.
    shipcountry = models.CharField(db_column='ShipCountry', max_length=15, blank=True, null=True) # Field name made lowercase.
    class Meta:
        db_table = 'orders'
