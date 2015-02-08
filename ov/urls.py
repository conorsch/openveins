from django.conf.urls import patterns, include, url
from django.contrib import admin
import haystack

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'openveins.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include('haystack.urls')),
)
