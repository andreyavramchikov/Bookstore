# -*- coding: utf-8 -*-
from django.db.models import Q
from catalog.models import Book
from models import SearchTerm

STRIP_WORDS = ['a','an','and','by','for','from','in','no','not','of','on','or','that','the','to','with']

def store(request, q):
    if len(q) > 2:
        term = SearchTerm()
        term.q = q
        term.ip_address = request.META.get('REMOTE_ADDR')
        term.user = None
        if request.user.is_authenticated():
            term.user = request.user
        term.save()


def books(search_text):
    words = _prepare_words(search_text)
    books = Book.active.all()
    results = {}
    results['books'] = []

    for word in words:
        books = books.filter( Q(name__icontains=word) | Q(description__icontains=word) |
                                    Q(sku__iexact=word) | Q(brand__icontains=word) |
                                    Q(meta_description__icontains=word) | Q(meta_keywords__icontains=word))
    results['books'] = books
    return results


def _prepare_words(search_text):
    words = search_text.split()
    for common in STRIP_WORDS:
        if common in words:
            words.remove(common)
    return words[0:5]
