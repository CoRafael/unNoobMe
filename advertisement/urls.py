__author__ = 'rafael'

from django.conf.urls import patterns, url

from advertisement import views


urlpatterns = patterns('',
                       url(r'^latest/$', views.latest_advertisement, name='latest'),
                       url(r'^interest/$', views.latest_interest, name='interest'),
                       url(r'^myadds/$', views.my_adds, name='myadds'),)

