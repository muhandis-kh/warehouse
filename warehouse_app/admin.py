from django.contrib import admin
from .models import Product, Material, ProductMaterial, Warehouse

# Register your models here.
@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ("product_name", 'product_code')
    
@admin.register(Material)
class Product(admin.ModelAdmin):
    list_display = ("material_name",)
    
@admin.register(ProductMaterial)
class Product(admin.ModelAdmin):
    list_display = ("product", 'material', 'quantity')
    
@admin.register(Warehouse)
class Product(admin.ModelAdmin):
    list_display = ("material", 'remainder', 'price')
