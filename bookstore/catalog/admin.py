from django.contrib import admin
from bookstore.catalog.forms import BookAdminForm
from bookstore.catalog.models import Book, Category, BookCategories
from bookstore.catalog.models import Publisher
from bookstore.catalog.models import Author, Address
import uuid
from catalog.models import OrderBookXref


def clone_book(modeladmin, request, queryset):
    books = queryset.all()
    for book in books:
        category = book.categories.all()[0]
        book.pk = None
        book.slug = uuid.uuid1().hex
        book.save()
        BookCategories.objects.create(book=book, category=category)

clone_book.short_description = "Clone selected books"

class BookAdmin(admin.ModelAdmin):
    form = BookAdminForm
    fields = ('name', 'price', 'image', 'quantity', 'description', 'author', 'publisher',)
    list_display = ('name', 'price', 'old_price', 'created_at', 'updated_at','button',)
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']
    actions = [clone_book]

    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    # sets up slug to be generated from book name
    # prepopulated_fields = {'slug' : ('name',)}



admin.site.register(Book, BookAdmin)


class CategoryAdmin(admin.ModelAdmin):
    #sets up values for how admin site lists categories
    list_display = ('name', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
# sets up slug to be generated from category name
    prepopulated_fields = {'slug' : ('name',)}

class OrderBookXrefAdmin(admin.ModelAdmin):
    list_display = ('book', 'order', 'quantity')
    readonly_fields = ('order',)
    raw_id_fields = ('book',)

admin.site.register(OrderBookXref, OrderBookXrefAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Publisher)
admin.site.register(Address)
admin.site.register(Author)
