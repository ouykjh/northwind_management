from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpRequest
from orders.models import Order
# Create your views here.
from .forms import OrderForm

def order(request):
	_id = request.POST.get("remove", "")
	if _id:
		id = _id.split('#');
		Order.objects.filter(id=int(id[1])).delete()

	return render_to_response("orders.html",
		 { 'orders' : Order.objects.all()} ,
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