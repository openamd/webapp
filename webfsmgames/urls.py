from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^arg/$', 'webfsmgames.arg.views.index'),
    (r'^arg/media/(?P<path>.*)$', 'django.views.static.serve',
    	{'document_root': 'C:/proj/py/webfsmgames/arg/media'}),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
