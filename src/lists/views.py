from django.shortcuts import render, render_to_response, RequestContext

# Create your views here.
def lists(request):
	return render_to_response("lists.html",
		context_instance=RequestContext(request),
		)