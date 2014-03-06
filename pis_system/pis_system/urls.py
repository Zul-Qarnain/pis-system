from django.conf.urls import patterns, include, url
from billing.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pis_system.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login$', login),
    url(r'^billing$', billing),
    url(r'^admin/', include(admin.site.urls)),
)
