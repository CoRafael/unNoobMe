from django.conf.urls import patterns, url

from rating import views


urlpatterns = patterns('',
                       url(r'^latest/$', views.latest_rating, name='rating'),
                       url(r'^rate_offer/$', views.rate_offer, name='rate_offer'),)