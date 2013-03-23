from django.conf.urls.defaults import *
urlpatterns = patterns('bookstore.cart.views',

        (r'^cart/', 'show_cart', { 'template_name':'cart/show_cart.html'}, 'show_cart'),

    )
