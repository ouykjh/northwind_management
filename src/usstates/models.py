from django.db import models

class Usstates(models.Model):
    stateid = models.SmallIntegerField(db_column='StateID') # Field name made lowercase.
    statename = models.CharField(db_column='StateName', max_length=100, blank=True) # Field name made lowercase.
    stateabbr = models.CharField(db_column='StateAbbr', max_length=2, blank=True) # Field name made lowercase.
    stateregion = models.CharField(db_column='StateRegion', max_length=50, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'usstates'

