from django.db import models

from regions.models import Region

class Territory(models.Model):
    territorydescription = models.CharField(db_column='TerritoryDescription', max_length=100) # Field name made lowercase.
    region = models.ForeignKey(Region)
    class Meta:
        db_table = 'territories'
