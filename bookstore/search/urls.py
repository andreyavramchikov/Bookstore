# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
urlpatterns = patterns('bookstore.search.views',
    (r'^results/$', 'results' , {'template_name': 'search/results.html'}, 'search_results'),
)
