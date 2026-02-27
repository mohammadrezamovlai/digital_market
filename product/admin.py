from django.contrib import admin
from .models import Product,File,Category,Cart,CartItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_active', 'count']
    list_filter = ['is_active']

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['product', 'file']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_time']

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'product', 'quantity', 'price']