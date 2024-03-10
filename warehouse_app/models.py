from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.product_name

class Material(models.Model):
    material_name = models.CharField(max_length=100)

    def __str__(self):
        return self.material_name

class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_materials')
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.product_name} - {self.material.material_name}"

class Warehouse(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    remainder = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.material.material_name} - {self.remainder} - {self.price}"


