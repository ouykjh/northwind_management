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

class EmployeeManger(models.Manager):
    def with_counts(self):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("""
            select employee_id, count(*) as count 
            from orders
            group by orders.employee_id
            order by 2 desc;""")
        result_list = []
        for row in cursor.fetchall():
            p = self.model( id=row[0])
            p.num_responses = row[1]
            result_list.append(p)
        return result_list

    def with_employees(self):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("""
            select customer_id, "HireDate", o.id from 
            orders o inner join employees e on o.employee_id = e.id 
            where e."HireDate" > '1992-05-01';""")
        result_list = []
        for row in cursor.fetchall():
            p = self.model( id=row[0], hireDate=row[1], orderid=row[2])
            result_list.append(p)
        return result_list

    def with_freight(self):
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("""
            select id, "OrderDate", "RequiredDate", "ShippedDate", "Freight"  
            from orders order by "Freight" 
            desc limit 10;""")
        result_list = []
        for row in cursor.fetchall():
            p = self.model( id=row[0], OrderDate=row[1], RequiredDate=row[2], ShippedDate=row[3], Freight=row[4])
            result_list.append(p)
        return result_list


class EmployeePool(models.Model):
    which = models.SmallIntegerField()
    objects = EmployeeManger()

class EmployeeHireDate(models.Model):
    which = models.CharField(max_length=40, blank=True, null=True)
    hireDate = models.DateField()
    orderid = models.SmallIntegerField()
    objects = EmployeeManger()

class OrdersTopFreight(models.Model):
    which = models.IntegerField()
    OrderDate = models.DateField()
    RequiredDate = models.DateField()
    ShippedDate = models.DateField()
    Freight = models.FloatField()
    objects = EmployeeManger()