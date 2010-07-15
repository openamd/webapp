# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from account.models import *

def settings(request):
    api = bool(other_service(request.user,"api_access","True"))    
    data = bool(other_service(request.user,"data_access","True"))
    if request.method == 'POST':
        if not request.POST.get('api_access', ''):
            update_other_services(request.user,api_access="")
        else:
            update_other_services(request.user,api_access="True")
        if not request.POST.get('data_access', ''):
            update_other_services(request.user,data_access="")
        else:
            update_other_services(request.user,data_access="True")
        return HttpResponseRedirect('/')
    return render_to_response('privacy_settings.html',
                              RequestContext(request,{"api_access":api,
                                                      "data_access":data,
                                                      }))
