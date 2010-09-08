# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect

import mining.cass
from account.models import update_other_services

def websites(request):
    if request.method == 'POST':
        webs = request.POST.get('websites', '')
        update_other_services(request.user, websites=webs)
    return HttpResponse(webs)

def clicks(request):
    pass

def stalker(request):
    pass
