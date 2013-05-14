from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from bookstore.cart import cart
from bookstore.catalog.forms import BookAddToCartForm
from bookstore.catalog.models import Category, Book


def index(request, template_name="catalog/index.html"):
    page_title = 'Musical Instruments and Sheet Music for Musicians'
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

def show_category(request, category_slug, template_name="catalog/category.html"):
    category = get_object_or_404(Category, slug=category_slug)
    books = category.book_set.all()
    page_title = category.name
    meta_keywords = category.meta_keywords
    meta_description = category.meta_description
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

def show_book(request, book_slug, template_name="catalog/book.html"):
    if request.method == "POST":
        postdata = request.POST.copy()
        form = BookAddToCartForm(request, postdata)
        if form.is_valid():
            '''add to cart and redirect to cart page'''
            cart.add_to_cart(request)
            return HttpResponseRedirect(reverse('show_cart'))
    else:
        '''get'''
        form = BookAddToCartForm()
        form.fields['book_slug'].widget.attrs['value'] = book_slug
        book = get_object_or_404(Book, slug=book_slug)
        categories = book.categories.filter(is_active=True)
        page_title = book.name
        meta_keywords = book.meta_keywords
        meta_description = book.meta_description
        return render_to_response(template_name, locals(),
                                  context_instance=RequestContext(request))
    
