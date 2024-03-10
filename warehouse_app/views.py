from rest_framework import generics
from .models import Product, Material, ProductMaterial, Warehouse
from .serializers import ProductSerializer, MaterialSerializer, ProductMaterialSerializer, WarehouseSerializer, ProductSerializerForMade
from rest_framework.response import Response
import json
from rest_framework import status

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class MaterialListView(generics.ListAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class ProductMaterialListView(generics.ListAPIView):
    queryset = ProductMaterial.objects.all()
    serializer_class = ProductMaterialSerializer

class WarehouseListView(generics.ListAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


from rest_framework.views import APIView
from rest_framework.response import Response


class CalculateMaterialsView(APIView):
    def post(self, request):
        #Kelgan requestdan mahsulot ma'lumotlarini olish
        products_data = request.data.get('products')

        # Ombordagi mahsulotlarni olish
        remaining_materials = Warehouse.objects.all().values('id', 'material__material_name', 'price', 'remainder')

        warehouse_data = []

        # So'rovdan kelgan querysetda kelgan ma'lumotlar bilan ishlashni qulaylashtirish maqsadida ma'lumotlar list ichidagi dict ko'rinishiga o'tkazib olindi
        for item in remaining_materials:

            warehouse_data.append({
                "warehouse_id": item['id'],
                "material_name": item['material__material_name'],
                "remainder": item['remainder'],
                "price": item['price']
            })
        result = self.calculate_materials(products_data, warehouse_data)

        return Response({"result": result})
    # Mahsulotlarga ketadigan xomashyoni hisoblash uchun funksiya
    def calculate_materials(self, products_data, warehouse_data):
        result = []
        remaining_materials = warehouse_data.copy()
        
        for product in products_data:
            product_name = product["product_name"]
            product_qty = product["product_qty"]
            product_materials = ProductMaterial.objects.filter(product__product_name=product_name).values('quantity', 'material__material_name',)

            
            used_materials = []
            for material in product_materials:
                material_name = material["material__material_name"]
                required_qty = material["quantity"] * product_qty
                
                # Depoda bulunan malzemeleri kontrol et
                remaining_qty = required_qty
                for warehouse_material in remaining_materials[:]:
                    if warehouse_material["material_name"] == material_name:
                        available_qty = warehouse_material["remainder"]
                        if available_qty >= remaining_qty:
                            used_qty = remaining_qty
                            remaining_qty = 0
                        else:
                            used_qty = available_qty
                            remaining_qty -= available_qty
                        
                        # Kullanılan malzemeyi güncelle ve ikinci ürüne dahil etme
                        warehouse_material["remainder"] -= used_qty
                        if warehouse_material["remainder"] == 0:
                            remaining_materials.remove(warehouse_material)
                        
                        used_materials.append({
                            "warehouse_id": warehouse_material["warehouse_id"],
                            "material_name": material_name,
                            "qty": used_qty,
                            "price": warehouse_material["price"]
                        })
                        
                        if remaining_qty == 0:
                            break
                
                # Eksik malzemeleri kontrol et
                if remaining_qty > 0:
                    used_materials.append({
                        "warehouse_id": None,
                        "material_name": material_name,
                        "qty": remaining_qty,
                        "price": None
                    })
            
            result.append({
                "product_name": product_name,
                "product_qty": product_qty,
                "product_materials": used_materials
            })
        
        return result