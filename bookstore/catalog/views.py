from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from catalog.models import Category, Product
from catalog.forms import ProductAddToCartForm
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from cart import cart

def index(request, template_name="catalog/index.html"):
    page_title = 'Musical Instruments and Sheet Music for Musicians'
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

def show_category(request, category_slug, template_name="catalog/category.html"):
    category = get_object_or_404(Category, slug=category_slug)
    products = category.product_set.all()
    page_title = category.name
    meta_keywords = category.meta_keywords
    meta_description = category.meta_description
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

def show_product(request, product_slug, template_name="catalog/product.html"):
    if request.method == "POST":
        postdata = request.POST.copy()
        form = ProductAddToCartForm(request, postdata)
        if form.is_valid():
            '''add to cart and redirect to cart page'''
            cart.add_to_cart(request)
            return HttpResponseRedirect(reverse('show_cart'))
    else:
        '''get'''
        form = ProductAddToCartForm()
        form.fields['product_slug'].widget.attrs['value'] = product_slug
        product = get_object_or_404(Product, slug=product_slug)
        categories = product.categories.filter(is_active=True)
        page_title = product.name
        meta_keywords = product.meta_keywords
        meta_description = product.meta_description
        return render_to_response(template_name, locals(),
                                  context_instance=RequestContext(request))
    
