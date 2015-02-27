__author__ = 'rafael'

from django.conf.urls import patterns, url

from base import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^logout/$', views.user_logout, name='logout'), )

