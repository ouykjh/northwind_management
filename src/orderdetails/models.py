from django.db import models

from orders.models import Order
from products.models import Product

class OrderDetail(models.Model):
	order = models.ForeignKey(Order)
	product = models.ForeignKey(Product)
	unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True) # Field name made lowercase.
	quantity = models.SmallIntegerField(db_column='Quantity', blank=True, null=True) # Field name made lowercase.
	discount = models.FloatField(db_column='Discount', blank=True, null=True)
	class Meta:
		db_table = 'order_details'
