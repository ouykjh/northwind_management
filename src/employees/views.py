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

def searchEmployee(request):
	context = RequestContext(request)

	if request.method == 'POST':
		Id = request.POST['Id']
		LastName = request.POST['LastName']
		FirstName = request.POST['FirstName']
		Title = request.POST['Title']
		Address = request.POST['Address']

		if LastName == None:
			LastName = r".*"

		if FirstName == None:
			FirstName = r".*"
		
		if Title == None:
			Title = r".*"

		if Address == None:
			Address = r".*"

		if Id:
			employees =  Employee.objects.filter(pk = Id,
												 lastname__regex=LastName,
												 firstname__regex=FirstName,
												 title__regex=Title,
												 address__regex=Address)
		else:
			employees =  Employee.objects.filter(lastname__regex=LastName,
												 firstname__regex=FirstName,
												 title__regex=Title,
												 address__regex=Address)

		return render_to_response("employeeOutcome.html",
									locals(),
									context_instance=RequestContext(request))

	return render_to_response("searchEmployee.html",
								locals(),
								context_instance=RequestContext(request))
