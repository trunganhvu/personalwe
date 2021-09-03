from django.db import models
from mainapp.model.Product import Product

class ProductImage(models.Model):
    """
    trunganhvu 2021/08/29
    """
    product_image_id = models.AutoField(primary_key=True)
    product_image_name = models.CharField(max_length=255)
    product_image_path = models.CharField(max_length=255)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        app_label = "mainapp"