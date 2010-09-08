from django.conf.urls.defaults import *
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

from account.openid_consumer import PinaxConsumer
#from waitinglist.forms import WaitingListEntryForm

# @@@ turn into template tag
def homepage(request):
    if request.method == "POST":
        #form = WaitingListEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("waitinglist_sucess"))
    else:
        #form = WaitingListEntryForm()
	pass
    return direct_to_template(request, "homepage.html", {
        #"form": form,
    })

if settings.ACCOUNT_OPEN_SIGNUP:
    signup_view = "account.views.signup"
else:
    signup_view = "signup_codes.views.signup"

urlpatterns = patterns('',
    url(r'^$', homepage, name="home"),
    
    (r'^auth/', include('djangofoursquare.urls')),

    url(r'^success/$', direct_to_template, {"template": "waitinglist/success.html"}, name="waitinglist_sucess"),
    url(r'^register/$', direct_to_template, {"template": "register.html"}),
    url(r'^map$', direct_to_template, {"template": "map.html"}),
    url(r'^map_private$', direct_to_template, {"template": "map_private.html"}),

    url(r'^admin/invite_user/$', 'signup_codes.views.admin_invite_user', name="admin_invite_user"),
    url(r'^account/signup/$', signup_view, name="acct_signup"),

    url(r'^settings/', 'privacy.views.settings'),
    
    (r'^about/', include('about.urls')),
    (r'^account/', include('account.urls')),
    (r'^openid/(.*)', PinaxConsumer()),

    (r'^profiles/', include('profiles.urls')),

    (r'^notices/', include('notification.urls')),
    (r'^messages/', include('messages.urls')),

    (r'^mining/', include('mining.urls')),

    (r'^avatar/', include('avatar.urls')),
    (r'^announcements/', include('announcements.urls')),
    
    (r'^admin/(.*)', admin.site.root),
)

"""
if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        (r'^site_media/', include('staticfiles.urls')),
    )
"""
