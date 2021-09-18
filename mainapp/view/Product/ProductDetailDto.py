from django.db import models
from mainapp.model.Product import Product
from mainapp.model.ProductSize import ProductSize
from mainapp.model.ProductColor import ProductColor

class ProductDetailDto(models.Model):
    """
    trunganhvu 2021/09/18
    """
    product_detail_id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_color_id = models.ForeignKey(ProductColor, on_delete=models.CASCADE)
    product_size_id = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    number_of_product = models.IntegerField(default=0)
    product_in_stock = models.IntegerField(default=0)
    product_original_price = models.DecimalField(max_digits=12, decimal_places=2)
    product_public_price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True, auto_now=True)