# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
import cart


def show_cart(request, template_name="cart/show_cart.html"):
    page_title = 'Musical Instruments and Sheet Music for Musicians'
    if request.method == 'POST':
        post_data = request.POST.copy()
        if post_data['submit'] == "Update":
            cart.update_cart(request)
        if post_data['submit'] == 'Remove':
            cart.remove_from_cart(request)

    cart_subtotal = cart.cart_subtotal(request)    
    cart_items =  cart.get_cart_items(request)
    
    
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))