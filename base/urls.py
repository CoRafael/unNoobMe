__author__ = 'rafael'

from django.conf.urls import patterns, url

from base import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'^latest/$', views.latest_advertisement, name='latest'),
                       url(r'^interest/$', views.latest_interest, name='interest'),)

