from django.db import models

from employees.models import Employee
from territories.models import Territory

class Employeeterritory(models.Model):
    employee = models.ForeignKey(Employee)
    territory = models.ForeignKey(Territory)
    class Meta:
        db_table = 'employeeterritories'
