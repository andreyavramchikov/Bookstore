from django.contrib import admin
from bookstore.catalog.forms import ProductAdminForm
from bookstore.catalog.models import Product, Category, ProductCategories
from bookstore.catalog.models import Publisher
from bookstore.catalog.models import Author, Address
import uuid


def clone_product(modeladmin, request, queryset):
    products = queryset.all()
    for product in products:
        category = product.categories.all()[0]
        product.pk = None
        product.slug = uuid.uuid1().hex
        product.save()
        ProductCategories.objects.create(product=product, category=category)

clone_product.short_description = "Clone selected products"


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    
    list_display = ('name', 'price', 'old_price', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']
    actions = [clone_product]


    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    # sets up slug to be generated from product name
    prepopulated_fields = {'slug' : ('name',)}
    
admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    #sets up values for how admin site lists categories
    list_display = ('name', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
# sets up slug to be generated from category name
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Publisher)
admin.site.register(Address)
admin.site.register(Author)
