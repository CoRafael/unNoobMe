__author__ = 'rafael'

from django.conf.urls import patterns, url

from noob import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'))
