# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from cart.models import CartItem
from catalog.models import OrderBookXref, Book
from order.models import Order


def proccess_order(request, template_name='order/order.html'):
    if request.method == 'POST':
        post_data = request.POST.copy()
        if post_data['submit'] == "Order":
            cart_id = post_data['cart_id']
            order = Order.objects.create()
            # simplejson have to be used
            cart_items = CartItem.objects.filter(cart_id=cart_id)
            for cart_item in cart_items:
                OrderBookXref.objects.create(book=cart_item.book, order=order, quantity=cart_item.quantity)
            cart_items.delete()


    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))