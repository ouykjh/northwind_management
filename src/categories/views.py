from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponseRedirect, HttpRequest
from .forms import CategoryForm
from categories.models import Category
# Create your views here.

def category(request):

	_id = request.POST.get("remove", "")
	if _id:
		id = _id.split('#');
		Category.objects.filter(id=int(id[1])).delete()

	return render_to_response("categories.html",
		 { 'categories' : Category.objects.all()} ,
		context_instance=RequestContext(request),
		)

def addCategory(request):

	form = CategoryForm(request.POST or None)

	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		return HttpResponseRedirect('categories')

	return render_to_response("addCategory.html",
								locals(),
								context_instance=RequestContext(request))