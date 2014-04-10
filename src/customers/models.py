from django.db import models

class Customer(models.Model):
    customerid = models.CharField(db_column='CustomerID', primary_key=True, max_length=10) # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=40, null=True) # Field name made lowercase.
    contactname = models.CharField(db_column='ContactName', max_length=30, blank=True, null=True) # Field name made lowercase.
    contacttitle = models.CharField(db_column='ContactTitle', max_length=30, blank=True, null=True) # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=60, blank=True, null=True) # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=15, blank=True, null=True) # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=15, blank=True, null=True) # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=10, blank=True, null=True) # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=15, blank=True, null=True) # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=24, blank=True, null=True) # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=24, blank=True, null=True) # Field name made lowercase.
    def __unicode__(self):
        return self.customerid
    class Meta:
        db_table = 'customers'