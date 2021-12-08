from django.contrib import admin

from .models import (
    Supplier,
    Buyer,
    Office,
    Drop,
    Product,
    Order,
    Delivery,
    ProductVariant,
    VariantOption
)


class SupplierAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'created_date']


class BuyerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'created_date']


admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Buyer, BuyerAdmin)
admin.site.register(Office)
admin.site.register(Drop)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Delivery)
admin.site.register(ProductVariant)
admin.site.register(VariantOption)
