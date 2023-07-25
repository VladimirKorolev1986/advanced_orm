from django.contrib import admin
from .models import Product, Order, OrderPosition


class OrderPositionInLine(admin.TabularInline):
    model = OrderPosition
    extra = 3


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price']
    list_filter = ['category']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id']
    inlines = [OrderPositionInLine, ]
