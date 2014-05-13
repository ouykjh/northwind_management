from django.shortcuts import render, render_to_response, RequestContext
from regions.models import Region
from django.http import HttpResponseRedirect, HttpRequest
from .forms import RegionForm
from categories.models import Category
from shippers.models import Shipper
from django.db import transaction, IntegrityError

# Create your views here.

def region(request):
	_id = request.POST.get("remove", "")
	if _id:
		id = _id.split('#');
		Region.objects.filter(id=int(id[1])).delete()

	elif request.method == 'POST':
		Id = request.POST['Id']
		Description = request.POST['Description']

		if Description == None:
			Description = r".*"


		if Id:
			regions =  Region.objects.filter(pk = Id,
											regiondescription__regex=Description)
		else:
			regions =  Region.objects.filter(regiondescription__regex=Description)

	else:
		regions = Region.objects.all()

	return render_to_response("regions.html",
								locals(),
								context_instance=RequestContext(request))

def addRegion(request):

	form = RegionForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		return HttpResponseRedirect('regions')

	return render_to_response("addRegion.html",
								locals(),
								context_instance=RequestContext(request))

@transaction.atomic
def atomicEmployeeAndOrder(request):
	if request.POST.get("atomic", ""):
		region = Region(pk = 5, regiondescription = "Polska");
		region.save();

		category = Category(categoryname="computers", description="super");
		category.save();

	if request.POST.get("savepoints", ""):
		region = Region(pk = 5, regiondescription = "Polska");
		region.save()
		try:
			spoint = transaction.savepoint()
		
			category = Category(categoryname="computers", description="super")
			category.save();
			raise Exception("I know python!")
			transaction.savepoint_commit(spoint)
		except Exception:
			transaction.savepoint_rollback(spoint) 


	return render_to_response("atomic.html",
						locals(),
						context_instance=RequestContext(request))