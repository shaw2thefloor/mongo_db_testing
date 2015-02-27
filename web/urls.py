__author__ = 'fshaw'
from django.conf.urls import patterns, include, url
from django.contrib import admin
from web import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add_author', views.add_author, name='add_author'),
    url(r'^show_author/(?P<author_id>[a-z0-9]+)', views.show_author, name='show_author'),
    url(r'^add_publication', views.add_publication, name='add_publication'),
    url(r'^delete_author/(?P<author_id>[a-z0-9]+)', views.delete_author, name='delete_author'),
    url(r'^delete_publication/(?P<publication_id>[a-z0-9]+)', views.delete_publication, name='delete_publication'),
)