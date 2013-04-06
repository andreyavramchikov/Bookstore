from django.conf.urls.defaults import *

urlpatterns = patterns('bookstore.accounts.views',
    (r'^register/$', 'register', {'template_name': 'registration/register.html'}, 'register'),

                      )

urlpatterns += patterns('django.contrib.auth.views',
    (r'^login/$', 'login', {'template_name': 'registration/login.html'}, 'login'),
                        )
