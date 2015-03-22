__author__ = 'crunchbang'

from django.conf.urls import patterns, url

from adv import views


urlpatterns = patterns('',
                       url(r'^(.*)/$', views.advertisement, name='advertisement'),
                      )

