from django.contrib import admin
from django.contrib.admin.options import TabularInline
from catalog.models import OrderProductXref
from order.models import Order, Delivery, Merchant


class OrderAdminInline(TabularInline):
    model = OrderProductXref
    fields = ('product', 'quantity')
    raw_id_fields = ('product',)
    readonly_fields = ('quantity',)
    extra = 0
    verbose_name_plural = "Order Products"
    verbose_name = "Order Products"

class DeliveryAdminInline(TabularInline):
    model = Merchant
    fields = ('first_name', 'last_name', )
    extra = 0
    verbose_name = 'Delivery Merchants'
    verbose_name_plural = 'Delivery Merchants'

class OrderAdmin(admin.ModelAdmin):
    # form = OrderAdminForm
    list_filter = ('active',)

    list_display = ('date_start', 'date_shipping',)
    inlines = [OrderAdminInline]

class DeliveryAdmin(admin.ModelAdmin):
    inlines = [DeliveryAdminInline]

admin.site.register(Order, OrderAdmin)
admin.site.register(Merchant)
admin.site.register(Delivery, DeliveryAdmin)