from django.conf.urls.defaults import *
urlpatterns = patterns('bookstore.order.views',
        (r'^order/', 'proccess_order', { 'template_name': 'order/order.html'}, 'order'),
    )
