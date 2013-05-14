from django.contrib import admin
from models import CartItem

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('book', 'quantity', 'date_added')
    readonly_fields = ('book', 'cart_id')

admin.site.register(CartItem, CartItemAdmin)