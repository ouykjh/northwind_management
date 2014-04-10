from django.db import models

class Region(models.Model):
    regiondescription = models.CharField(db_column='RegionDescription', max_length=10) # Field name made lowercase.
    class Meta:
        db_table = 'region'
