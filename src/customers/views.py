from django.shortcuts import render, render_to_response, RequestContext
from customers.models import Customer
from django.http import HttpResponseRedirect, HttpRequest
from .forms import CustomerForm
# Create your views here.

def customer(request):
	_id = request.POST.get("remove", "")
	if _id:
		Customer.objects.filter(customerid=str(_id)).delete()

	return render_to_response("customers.html",
		 { 'customers' : Customer.objects.all()} ,
		context_instance=RequestContext(request),
		)

def addCustomer(request):

	form = CustomerForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		return HttpResponseRedirect('customers')

	return render_to_response("addCustomer.html",
								locals(),
								context_instance=RequestContext(request))