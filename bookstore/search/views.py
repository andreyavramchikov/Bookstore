# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from bookstore.search import search

from django.core.paginator import Paginator, InvalidPage, EmptyPage
from bookstore import settings



def results(request, template_name="search/results.html"):
# get current search phrase
    q = request.GET.get('q', '')
# get current page number. Set to 1 is missing or invalid
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1
    matching = search.books(q).get('books')
    paginator = Paginator(matching,settings.PRODUCTS_PER_PAGE)
    try:
        results = paginator.page(page).object_list
    except (InvalidPage, EmptyPage):
        results = paginator.page(1).object_list
    # store the search
    search.store(request, q)
    # the usual...
    page_title = 'Search Results for: ' + q
    return render_to_response(template_name, locals(),
    context_instance=RequestContext(request))


