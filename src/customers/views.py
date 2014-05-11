from django.shortcuts import render, render_to_response, RequestContext
from customers.models import Customer
from django.http import HttpResponseRedirect, HttpRequest
from .forms import CustomerForm
# Create your views here.

def customer(request):
	_id = request.POST.get("remove", "")
	if _id:
		Customer.objects.filter(customerid=str(_id)).delete()

	elif request.method == 'POST':
		Id = request.POST['Id']
		CompanyName = request.POST['CompanyName']
		ContactName = request.POST['ContactName']
		Address = request.POST['Address']
		City = request.POST['City']
		Region = request.POST['Region']
		Phone = request.POST['Phone']

		if CompanyName == None:
			CompanyName = r".*"

		if ContactName == None:
			ContactName = r".*"
		
		if Address == None:
			Address = r".*"

		if City == None:
			City = r".*"

		if Region == None:
			Region = r".*"

		if Phone == None:
			Phone = r".*"



		if Id:
			customers =  Customer.objects.filter(pk = Id,
												 companyname__regex=CompanyName,
												 contactname__regex=ContactName,
												 address__regex=Address,
												 city__regex=City,
												 region__regex=Region,
												 phone__regex=Phone)
		else:
			customers =  Customer.objects.filter(companyname__regex=CompanyName,
												 contactname__regex=ContactName,
												 address__regex=Address,
												 city__regex=City,
												 region__regex=Region,
												 phone__regex=Phone)

	else:
		customers = Customer.objects.all()

	return render_to_response("customers.html",
								locals(),
								context_instance=RequestContext(request))

def addCustomer(request):

	form = CustomerForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		return HttpResponseRedirect('customers')

	return render_to_response("addCustomer.html",
								locals(),
								context_instance=RequestContext(request))