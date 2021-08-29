from django.db import models

class ProductColor(models.Model):
    """
    trunganhvu 2021/08/29
    """
    product_color_id = models.AutoField(primary_key=True)
    product_color_code = models.CharField(max_length=25)
    product_color_name = models.CharField(max_length=255)
    created_at = models.DateField(null=False)
    updated_at = models.DateField(null=True)

    class Meta:
        app_label = "mainapp"