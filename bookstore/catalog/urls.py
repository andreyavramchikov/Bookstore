from django.conf.urls.defaults import *
urlpatterns = patterns('bookstore.catalog.views',

        (r'^$', 'index', { 'template_name':'catalog/index.html'}, 'catalog_home'),
        
        (r'^category/(?P<category_slug>[-\w]+)/$', 'show_category', 
                    {'template_name':'catalog/category.html'}, 'catalog_category'),
                       
        (r'^book/(?P<book_slug>[-\w]+)/$', 'show_book',
                    {'template_name':'catalog/book.html'},'catalog_book'),
    )
