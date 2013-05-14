from django.contrib import admin
from django.contrib.admin.options import TabularInline
from catalog.models import OrderBookXref, DeliveryBookXref
from order.models import Order, Delivery, Merchant


class OrderAdminInline(TabularInline):
    model = OrderBookXref
    fields = ('book', 'quantity')
    raw_id_fields = ('book',)
    readonly_fields = ('quantity',)
    extra = 0
    verbose_name_plural = "Order Books"
    verbose_name = "Order Books"

class DeliveryAdminInline(TabularInline):
    model = DeliveryBookXref
    extra = 0
    # fields = ('first_name', 'last_name', 'date_shipping' )
    # extra = 0
    # verbose_name = 'Delivery Merchants'
    # verbose_name_plural = 'Delivery Merchants'

class OrderAdmin(admin.ModelAdmin):
    # form = OrderAdminForm
    list_filter = ('active',)

    list_display = ('date_start', 'date_shipping',)
    inlines = [OrderAdminInline]

class DeliveryAdmin(admin.ModelAdmin):
    # fields = ('name', 'description', 'date_shipping', 'is_payed', 'is_delivered')
    inlines = [DeliveryAdminInline]

admin.site.register(Order, OrderAdmin)
admin.site.register(Merchant)
admin.site.register(Delivery, DeliveryAdmin)