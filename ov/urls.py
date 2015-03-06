from django.conf.urls import patterns, include, url
from django.contrib import admin
from openveins.views import QuoteCreateView, QuoteUpdateView


urlpatterns = patterns('',
    # Home page
    url(r'^$', 'openveins.views.home', name='home'),
    # General admin functionality
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include('haystack.urls')),

    # Support user logins
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),

    # Manage Quote objects
    url(r'^about/', 'openveins.views.about', name='about'),
    url(r'^new/', QuoteCreateView.as_view(), name='new-quote'),
    url(r'^edit/(?P<pk>.+)', QuoteUpdateView.as_view(), name='edit-quote'),
)
