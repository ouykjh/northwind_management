# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class ArticleArticle(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField()
    likes = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'article_article'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        managed = False
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        managed = False
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'

class Categories(models.Model):
    categoryid = models.SmallIntegerField(db_column='CategoryID', primary_key=True) # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=15) # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True) # Field name made lowercase.
    picture = models.BinaryField(db_column='Picture', blank=True, null=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'categories'

class Customercustomerdemo(models.Model):
    customerid = models.CharField(db_column='CustomerID', max_length=-1) # Field name made lowercase.
    customertypeid = models.CharField(db_column='CustomerTypeID', max_length=-1) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'customercustomerdemo'

class Customerdemographics(models.Model):
    customertypeid = models.CharField(db_column='CustomerTypeID', primary_key=True, max_length=-1) # Field name made lowercase.
    customerdesc = models.TextField(db_column='CustomerDesc', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'customerdemographics'

class Customers(models.Model):
    customerid = models.CharField(db_column='CustomerID', primary_key=True, max_length=-1) # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=40) # Field name made lowercase.
    contactname = models.CharField(db_column='ContactName', max_length=30, blank=True) # Field name made lowercase.
    contacttitle = models.CharField(db_column='ContactTitle', max_length=30, blank=True) # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=60, blank=True) # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=15, blank=True) # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=15, blank=True) # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=10, blank=True) # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=15, blank=True) # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=24, blank=True) # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=24, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'customers'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    class Meta:
        managed = False
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'django_site'

class Employees(models.Model):
    employeeid = models.SmallIntegerField(db_column='EmployeeID', primary_key=True) # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=20) # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=10) # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=30, blank=True) # Field name made lowercase.
    titleofcourtesy = models.CharField(db_column='TitleOfCourtesy', max_length=25, blank=True) # Field name made lowercase.
    birthdate = models.DateField(db_column='BirthDate', blank=True, null=True) # Field name made lowercase.
    hiredate = models.DateField(db_column='HireDate', blank=True, null=True) # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=60, blank=True) # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=15, blank=True) # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=15, blank=True) # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=10, blank=True) # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=15, blank=True) # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=24, blank=True) # Field name made lowercase.
    extension = models.CharField(db_column='Extension', max_length=4, blank=True) # Field name made lowercase.
    photo = models.BinaryField(db_column='Photo', blank=True, null=True) # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True) # Field name made lowercase.
    reportsto = models.SmallIntegerField(db_column='ReportsTo', blank=True, null=True) # Field name made lowercase.
    photopath = models.CharField(db_column='PhotoPath', max_length=255, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'employees'

class Employeeterritories(models.Model):
    employeeid = models.SmallIntegerField(db_column='EmployeeID') # Field name made lowercase.
    territoryid = models.CharField(db_column='TerritoryID', max_length=20) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'employeeterritories'

class OrderDetails(models.Model):
    orderid = models.SmallIntegerField(db_column='OrderID') # Field name made lowercase.
    productid = models.SmallIntegerField(db_column='ProductID') # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice') # Field name made lowercase.
    quantity = models.SmallIntegerField(db_column='Quantity') # Field name made lowercase.
    discount = models.FloatField(db_column='Discount') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'order_details'

class OrderOrder(models.Model):
    id = models.IntegerField(primary_key=True)
    orderdate = models.DateField(db_column='OrderDate') # Field name made lowercase.
    requireddate = models.DateField(db_column='RequiredDate') # Field name made lowercase.
    shippeddate = models.DateField(db_column='ShippedDate') # Field name made lowercase.
    shipvia = models.IntegerField(db_column='ShipVia') # Field name made lowercase.
    shipname = models.CharField(db_column='ShipName', max_length=200) # Field name made lowercase.
    shipaddres = models.CharField(db_column='ShipAddres', max_length=200) # Field name made lowercase.
    shipcity = models.CharField(db_column='ShipCity', max_length=200) # Field name made lowercase.
    shipregion = models.CharField(db_column='ShipRegion', max_length=200) # Field name made lowercase.
    shippostalcode = models.CharField(db_column='ShipPostalCode', max_length=200) # Field name made lowercase.
    shipcounter = models.CharField(db_column='ShipCounter', max_length=200) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'order_order'

class Orders(models.Model):
    orderid = models.SmallIntegerField(db_column='OrderID', primary_key=True) # Field name made lowercase.
    customerid = models.CharField(db_column='CustomerID', max_length=-1, blank=True) # Field name made lowercase.
    employeeid = models.SmallIntegerField(db_column='EmployeeID', blank=True, null=True) # Field name made lowercase.
    orderdate = models.DateField(db_column='OrderDate', blank=True, null=True) # Field name made lowercase.
    requireddate = models.DateField(db_column='RequiredDate', blank=True, null=True) # Field name made lowercase.
    shippeddate = models.DateField(db_column='ShippedDate', blank=True, null=True) # Field name made lowercase.
    shipvia = models.SmallIntegerField(db_column='ShipVia', blank=True, null=True) # Field name made lowercase.
    freight = models.FloatField(db_column='Freight', blank=True, null=True) # Field name made lowercase.
    shipname = models.CharField(db_column='ShipName', max_length=40, blank=True) # Field name made lowercase.
    shipaddress = models.CharField(db_column='ShipAddress', max_length=60, blank=True) # Field name made lowercase.
    shipcity = models.CharField(db_column='ShipCity', max_length=15, blank=True) # Field name made lowercase.
    shipregion = models.CharField(db_column='ShipRegion', max_length=15, blank=True) # Field name made lowercase.
    shippostalcode = models.CharField(db_column='ShipPostalCode', max_length=10, blank=True) # Field name made lowercase.
    shipcountry = models.CharField(db_column='ShipCountry', max_length=15, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'orders'

class Products(models.Model):
    productid = models.SmallIntegerField(db_column='ProductID', primary_key=True) # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=40) # Field name made lowercase.
    supplierid = models.SmallIntegerField(db_column='SupplierID', blank=True, null=True) # Field name made lowercase.
    categoryid = models.SmallIntegerField(db_column='CategoryID', blank=True, null=True) # Field name made lowercase.
    quantityperunit = models.CharField(db_column='QuantityPerUnit', max_length=20, blank=True) # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice', blank=True, null=True) # Field name made lowercase.
    unitsinstock = models.SmallIntegerField(db_column='UnitsInStock', blank=True, null=True) # Field name made lowercase.
    unitsonorder = models.SmallIntegerField(db_column='UnitsOnOrder', blank=True, null=True) # Field name made lowercase.
    reorderlevel = models.SmallIntegerField(db_column='ReorderLevel', blank=True, null=True) # Field name made lowercase.
    discontinued = models.IntegerField(db_column='Discontinued') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'products'

class Region(models.Model):
    regionid = models.SmallIntegerField(db_column='RegionID', primary_key=True) # Field name made lowercase.
    regiondescription = models.CharField(db_column='RegionDescription', max_length=-1) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'region'

class Shippers(models.Model):
    shipperid = models.SmallIntegerField(db_column='ShipperID', primary_key=True) # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=40) # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=24, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'shippers'

class ShippersTmp(models.Model):
    shipperid = models.SmallIntegerField(db_column='ShipperID', primary_key=True) # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=40) # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=24, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'shippers_tmp'

class SignupsSignup(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=120, blank=True)
    last_name = models.CharField(max_length=120, blank=True)
    email = models.CharField(max_length=75)
    timestamp = models.DateTimeField()
    updated = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'signups_signup'

class Suppliers(models.Model):
    supplierid = models.SmallIntegerField(db_column='SupplierID', primary_key=True) # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=40) # Field name made lowercase.
    contactname = models.CharField(db_column='ContactName', max_length=30, blank=True) # Field name made lowercase.
    contacttitle = models.CharField(db_column='ContactTitle', max_length=30, blank=True) # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=60, blank=True) # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=15, blank=True) # Field name made lowercase.
    region = models.CharField(db_column='Region', max_length=15, blank=True) # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=10, blank=True) # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=15, blank=True) # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=24, blank=True) # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=24, blank=True) # Field name made lowercase.
    homepage = models.TextField(db_column='HomePage', blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'suppliers'

class Territories(models.Model):
    territoryid = models.CharField(db_column='TerritoryID', primary_key=True, max_length=20) # Field name made lowercase.
    territorydescription = models.CharField(db_column='TerritoryDescription', max_length=-1) # Field name made lowercase.
    regionid = models.SmallIntegerField(db_column='RegionID') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'territories'

class Usstates(models.Model):
    stateid = models.SmallIntegerField(db_column='StateID') # Field name made lowercase.
    statename = models.CharField(db_column='StateName', max_length=100, blank=True) # Field name made lowercase.
    stateabbr = models.CharField(db_column='StateAbbr', max_length=2, blank=True) # Field name made lowercase.
    stateregion = models.CharField(db_column='StateRegion', max_length=50, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'usstates'

