from django.shortcuts import render

# Create your views here.
#from sol3.home import views

from django.shortcuts import render_to_response
from django.template import RequestContext
 
def index(request):
    return render_to_response('home/index.html', context_instance=RequestContext(request))