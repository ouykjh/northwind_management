from django.shortcuts import render, render_to_response, RequestContext
from suppliers.models import Supplier
# Create your views here.

def seafoodSuppliers(request):
	seafood = 'Seafood'
	supp = Supplier.objects.raw('select distinct s.id, s."CompanyName", s."ContactName", s."ContactTitle", s."City", s."Region", s."PostalCode", s."Country", s."Phone", s."Fax", s."HomePage"  from suppliers as s inner join products as p on (s.id = p."supplier_id") inner join categories as c on (c.id = p."category_id") where c."CategoryName" = %s order by s.id;' , [seafood])
	return render_to_response("seafoodSuppliers.html",
		 { 'sfSuppliers' : supp} ,
		context_instance=RequestContext(request),
		)