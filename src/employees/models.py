from django.db import models

class Employee(models.Model):
    lastname = models.CharField(db_column='LastName', max_length=20) # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=10) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=30, blank=True, null=True) # Field name made lowercase.
    titleofcourtesy = models.CharField(db_column='TitleOfCourtesy', max_length=25, blank=True, null=True) # Field name made lowercase.
    birthdate = models.DateField(db_column='BirthDate', blank=True, null=True) # Field name made lowercase.
    hiredate = models.DateField(db_column='HireDate', blank=True, null=True) # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=60, blank=True, null=True) # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=15, blank=True, null=True) # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=15, blank=True, null=True) # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=10, blank=True, null=True) # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=15, blank=True, null=True) # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=24, blank=True, null=True) # Field name made lowercase.
    extension = models.CharField(db_column='Extension', max_length=4, blank=True, null=True) # Field name made lowercase.
    photo = models.BinaryField(db_column='Photo', blank=True, null=True) # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True) # Field name made lowercase.
    reportsto = models.SmallIntegerField(db_column='ReportsTo', blank=True, null=True) # Field name made lowercase.
    photopath = models.CharField(db_column='PhotoPath', max_length=255, blank=True, null=True) # Field name made lowercase.
    def __unicode__(self):
        return self.id
    class Meta:
        db_table = 'employees'


