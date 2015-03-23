__author__ = 'crunchbang'

from django.conf.urls import patterns, url

from adv import views


urlpatterns = patterns('',
                       url(r'^$', views.add_offer, name='offer'),
                       url(r'^(.*)/$', views.advertisement, name='advertisement'), )

