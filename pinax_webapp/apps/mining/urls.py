from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^stalker/$', 'mining.views.stalker', name="mining_stalker"),
    url(r'^clicks/$', 'mining.views.clicks',name="mining_clicks"),
    url(r'^websites/$', 'mining.views.websites',name="mining_websites"),
)
