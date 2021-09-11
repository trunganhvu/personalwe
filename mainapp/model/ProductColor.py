from django.db import models
from mainapp.model.ProductType import ProductType

class ProductColor(models.Model):
    """
    trunganhvu 2021/08/29
    """
    product_color_id = models.AutoField(primary_key=True)
    product_type_id = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    product_color_code = models.CharField(max_length=25)
    product_color_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        app_label = "mainapp"