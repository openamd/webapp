from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^username_autocomplete/$', 'autocomplete_app.views.username_autocomplete_friends', name='profile_username_autocomplete'),
    url(r'^$', 'profiles.views.profiles', name='profile_list'),
    url(r'^friends/(?P<username>[\w\._-]+)/$', 'profiles.views.profile', {'t' : 'profiles/friends.html'} , name='profile_detail'),
    #profile after friends so the reverse url finds it
    url(r'^profile/(?P<username>[\w\._-]+)/$', 'profiles.views.profile', name='profile_detail'),
    url(r'^edit/$', 'profiles.views.profile_edit', name='profile_edit'),
)
