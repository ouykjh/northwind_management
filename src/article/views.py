from django.shortcuts import render, render_to_response, RequestContext

# Create your views here.
def Article(request):
	return render_to_response("article.html",
								locals(),
								context_instance=RequestContext(request))