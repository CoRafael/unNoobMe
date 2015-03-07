from django.conf.urls import patterns, url

from rating import views


urlpatterns = patterns('',
                       url(r'^(.*)/$', views.latest_rating, name='rating'),)