from django.db import models

class ProductType(models.Model):
    """
    trunganhvu 2021/08/29
    """
    product_type_id = models.AutoField(primary_key=True)
    product_type_code = models.CharField(max_length=25)
    product_type_name = models.CharField(max_length=255)
    product_type_description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        app_label = "mainapp"