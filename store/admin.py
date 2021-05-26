from django.contrib import admin
from .models import Product, Cover

class CoverAdmin(admin.ModelAdmin):
    list_display = ('ad_name', 'ad_text')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)
admin.site.register(Cover)
