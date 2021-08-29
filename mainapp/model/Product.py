from django.db import models
from mainapp.model.ProductType import ProductType

class Product(models.Model):
    """
    trunganhvu 2021/08/29
    """
    product_id = models.AutoField(primary_key=True)
    product_code = models.CharField(max_length=25)
    product_name = models.CharField(max_length=255)
    product_type_id = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    product_description = models.CharField(max_length=1000)
    product_detail = models.CharField(max_length=1000)
    created_at = models.DateField(null=False)
    updated_at = models.DateField(null=True)

    class Meta:
        app_label = "mainapp"