from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpRequest
from orders.models import Order
from orders.models import EmployeeManger, EmployeePool,EmployeeHireDate, OrdersTopFreight
from regions.models import Region

# Create your views here.
from .forms import OrderForm

def order(request):
	_id = request.POST.get("remove", "")
	if _id:
		id = _id.split('#');
		Order.objects.filter(id=int(id[1])).delete()

	orders = Order.objects.all()

	return render_to_response("orders.html",
		 locals(),
		context_instance=RequestContext(request),
		)

def addOrder(request):

	form = OrderForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		return HttpResponseRedirect('orders')

	return render_to_response("addOrder.html",
								locals(),
								context_instance=RequestContext(request))

def ordersManager(request):
	return render_to_response("ordersManager.html",
								locals(),
								context_instance=RequestContext(request))

def ordersPerEmployee(request):
	orders =  EmployeePool.objects.with_counts()
	return render_to_response("ordersPerEmployee.html",
							locals(),
							context_instance=RequestContext(request))

def employeesHireDate(request):
	customers =  EmployeeHireDate.objects.with_employees()
	return render_to_response("employeesHireDate.html",
							locals(),
							context_instance=RequestContext(request))

def ordersFreightTop(request):
	customers =  OrdersTopFreight.objects.with_freight()
	return render_to_response("ordersFreightTop.html",
							locals(),
							context_instance=RequestContext(request))

