from django.contrib import admin
from .models import Product, ProductVariations


class ProductAdmin(admin.ModelAdmin):
    list_display = ['prod_name', 'slug', 'stock',
                    'is_available', 'price', 'create_date',
                    'image', 'category']
    ordering = ['-create_date']
    prepopulated_fields = {
        'slug': ('prod_name',)
    }


class VariationAdmin(admin.ModelAdmin):
    list_display = [
         'variations', 'value', 'is_active'
    ]
    list_editable = ['is_active']
    list_filter = ['variations', 'value']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductVariations, VariationAdmin)
