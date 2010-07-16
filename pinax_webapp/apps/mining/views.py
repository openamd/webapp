# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse,HttpResponseRedirect

import mining.cass

def websites(request):
    if request.method == 'POST':
        webs = request.POST.get('websites', '')
        mining.cass.update_user_field(request.user.username,
                                      'websites',
                                      webs)
    return HttpResponse(webs)

def clicks(request):
    pass

def stalker(request):
    pass
