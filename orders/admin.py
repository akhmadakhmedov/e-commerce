from django.contrib import admin

from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'phone_number', 'city', 'order_total', 'delivery_fee', 'status', 'is_ordered', 'created_at']
    list_filter = ['status', 'is_ordered']
    search_fields = ['order_number', 'name', 'surname', 'phone_number']
    list_per_page = 20

admin.site.register(Order, OrderAdmin)


