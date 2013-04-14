from django.conf.urls import patterns, include, url
from django.views.static import * 
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     (r'^', include('bookstore.catalog.urls')),
     (r'^', include('bookstore.cart.urls')),
     (r'^accounts/', include('bookstore.accounts.urls')),
     (r'^accounts/', include('django.contrib.auth.urls')),
     (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
     (r'^admin/', include(admin.site.urls)),
)
