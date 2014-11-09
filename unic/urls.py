from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'unic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^enquiries/', include(admin.site.urls)),
    url(r'', include('enquiry.urls')),
)
