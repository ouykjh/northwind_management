from django.shortcuts import render, render_to_response, RequestContext
from regions.models import Region
from django.http import HttpResponseRedirect, HttpRequest
from .forms import RegionForm

# Create your views here.

def region(request):
	_id = request.POST.get("remove", "")
	if _id:
		id = _id.split('#');
		Region.objects.filter(id=int(id[1])).delete()

	return render_to_response("regions.html",
		 { 'regions' : Region.objects.all()} ,
		context_instance=RequestContext(request),
		)

def addRegion(request):

	form = RegionForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		return HttpResponseRedirect('regions')

	return render_to_response("addRegion.html",
								locals(),
								context_instance=RequestContext(request))