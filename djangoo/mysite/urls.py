from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from musicshare.models import song
from django.views.generic import DetailView, ListView
from django.contrib.auth.models import User


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
#admin.site.unregister(User)

urlpatterns = patterns('',
        # Examples:
        # url(r'^$', 'mysite.views.home', name='home'),
        # url(r'^mysite/', include('mysite.foo.urls')),

        # Uncomment the admin/doc line below to enable admin documentation:
        url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
        url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        url(r'^$','musicshare.views.home'),
        url(r'^submit/','musicshare.views.submit'),
        # Uncomment the next line to enable the admin:
        url(r'^artist/$','musicshare.views.artistView'),
        url(r'^user/new$','musicshare.views.newUser'),
        url(r'^record/new$','musicshare.views.newRecord'),
        url(r'^artist/new$','musicshare.views.newArtist'),
        url(r'^album/new$','musicshare.views.newAlbum'),
        url(r'^song/new$','musicshare.views.newSong'),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
        url(r'^user/(?P<pk>\d+)/edit','musicshare.views.editUser'),

        url(r'^admin/', include(admin.site.urls)),
        )
