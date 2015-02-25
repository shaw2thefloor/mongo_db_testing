__author__ = 'fshaw'
from django.conf.urls import patterns, include, url
from django.contrib import admin
from web import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mongoTest.views.home', name='home'),
    url(r'^$', views.index, name='index'),
    url(r'^add_author', views.add_author),
    url(r'^show_author/(?P<author_id>[a-z0-9]+)', views.show_author, name='show_author'),
)