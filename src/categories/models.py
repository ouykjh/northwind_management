from django.db import models

class Category(models.Model):
    categoryname = models.CharField(db_column='CategoryName', max_length=15) # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True) # Field name made lowercase.
    picture = models.BinaryField(db_column='Picture', blank=True, null=True) # Field name made lowercase.
    def __unicode__(self):
		return self.CategoryName
    class Meta:
        db_table = 'categories'

