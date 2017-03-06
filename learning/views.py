from django.shortcuts import render 
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404, render 
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def home(request):
    
    args = {}
    args['home'] = "Home" 

    return render(request, 'learning_home.html', args) 
