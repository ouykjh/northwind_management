from django.shortcuts import render, render_to_response, RequestContext
from employees.models import Employee
from django.http import HttpResponseRedirect, HttpRequest
from .forms import EmployeeForm

# Create your views here.

def employee(request):
	_id = request.POST.get("remove", "")
	if _id:
		id = _id.split('#');
		Employee.objects.filter(id=int(id[1])).delete()

	return render_to_response("employees.html",
		 { 'employees' : Employee.objects.all()} ,
		context_instance=RequestContext(request),
		)

def addEmployee(request):

	form = EmployeeForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		return HttpResponseRedirect('employees')

	return render_to_response("addEmployee.html",
								locals(),
								context_instance=RequestContext(request))