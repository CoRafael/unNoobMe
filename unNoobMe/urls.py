from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^advertisement/', include('advertisement.urls')),
                       url(r'^addadvertisement/', include('addadvertisement.urls')),
                       url(r'^user/', include('userprofile.urls')),
                       url(r'^rating/', include('rating.urls')),
                       url('^adv/', include('adv.urls')),
                       url('', include('base.urls')), )


# UNDERNEATH your urlpatterns definition, advertisement the following two lines:
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
         'serve',
         {'document_root': settings.MEDIA_ROOT}), )