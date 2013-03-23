# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext


def show_cart(request, template_name="cart/show_cart.html"):
    page_title = 'Musical Instruments and Sheet Music for Musicians'
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))