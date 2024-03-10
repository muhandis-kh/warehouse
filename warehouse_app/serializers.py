from rest_framework import serializers
from .models import Product, Material, ProductMaterial, Warehouse

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'product_code']

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'material_name']

class ProductMaterialSerializer(serializers.ModelSerializer):
    # Mahsulot va xomashyolarni id raqamlari bo'yicha emas nomlari bo'yicha saralash uchun serializerga bu bo'limlar qo'shildi
    product_name = serializers.CharField(source='product.product_name')
    material_name = serializers.CharField(source='material.material_name')
    class Meta:
        model = ProductMaterial
        fields = ['id','product_name', 'material_name', 'quantity']

class WarehouseSerializer(serializers.ModelSerializer):
    material_name = serializers.CharField(source='material.material_name')
    
    class Meta:
        model = Warehouse
        fields = ['id', 'material_name', 'remainder', 'price']
        
class ProductSerializerForMade(serializers.Serializer):
    product_name = serializers.CharField()
    product_qty = serializers.IntegerField()