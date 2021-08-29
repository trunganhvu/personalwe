from django.db import models
from mainapp.model.ProductType import ProductType

class ProductSize(models.Model):
    """
    trunganhvu 2021/08/29
    """
    product_size_id = models.AutoField(primary_key=True)
    product_size_code = models.CharField(max_length=25)
    product_size_name = models.CharField(max_length=255)
    product_type_id = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    product_size_height_max = models.IntegerField(default=0)
    product_size_height_min = models.IntegerField(default=0)
    product_size_width_max = models.IntegerField(default=0)
    product_size_width_min = models.IntegerField(default=0)
    created_at = models.DateField(null=False)
    updated_at = models.DateField(null=True)

    class Meta:
        app_label = "mainapp"