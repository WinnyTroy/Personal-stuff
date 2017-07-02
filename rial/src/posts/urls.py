from django.conf.urls import url
from django.contrib import admin


from .views import *

urlpatterns = [
    url(r'^$', post_list, name='index'),
    url(r'^create/$', post_create, name='create'),
    url(r'^(?P<slug>[\w\-]+)/$', post_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', post_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', post_delete),
]
