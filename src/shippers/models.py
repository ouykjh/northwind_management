from django.db import models

class Shipper(models.Model):
    companyname = models.CharField(db_column='CompanyName', max_length=40) # Field name made lowercase.
    phone = models.CharField(db_column="Phone", max_length=24, null=False)
    class Meta:
        db_table = 'shipper'
