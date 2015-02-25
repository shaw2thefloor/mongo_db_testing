from django.conf.urls import patterns, include, url
from django.contrib import admin
from web import urls


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project_copo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^mongo/', include('web.urls', namespace='mongo')),

)
