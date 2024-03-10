from django.urls import path
from .views import ProductListView, MaterialListView, ProductMaterialListView, WarehouseListView, CalculateMaterialsView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('materials/', MaterialListView.as_view(), name='material-list'),
    path('product-materials/', ProductMaterialListView.as_view(), name='product-material-list'),
    path('warehouses/', WarehouseListView.as_view(), name='warehouse-list'),
    path('check/', CalculateMaterialsView.as_view(), name='check'),
]
