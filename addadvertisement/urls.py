__author__ = 'rafael'

from django.conf.urls import patterns, url

from addadvertisement import views


urlpatterns = patterns('',
                       url(r'^$', views.add_advertisement, name='addadvertisement'),
                       url(r'^test/$', views.test, name='test'),)

