from django.shortcuts import render, render_to_response, RequestContext
from products.models import Product
# Create your views here.

def year1998OrderProducts(request):
	startDate = '1997-12-31'
	endDate = '1999-01-01'
	yearProducts = Product.objects.raw('select distinct p.id, p."ProductName", p."QuantityPerUnit", p."UnitPrice", p."UnitsInStock", p."UnitsOnOrder", p."ReorderLevel", p."Discontinued" from products as p inner join order_details as od on (p.id = od."product_id") inner join orders as o on (od."order_id" = o.id) where o."OrderDate" > %s and o."OrderDate" < %s order by p.id;', [startDate, endDate])

	return render_to_response("yearProducts.html",
		 { 'yearProducts' : yearProducts} ,
		context_instance=RequestContext(request),
		)