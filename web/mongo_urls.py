__author__ = 'fshaw'
from django.conf.urls import patterns, include, url
from django.contrib import admin
from web import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mongoTest.views.home', name='home'),
    url(r'^$', views.index),

)
