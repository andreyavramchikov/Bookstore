from django.contrib import admin
from models import CartItem

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'date_added')
    readonly_fields = ('product', 'cart_id')

admin.site.register(CartItem, CartItemAdmin)