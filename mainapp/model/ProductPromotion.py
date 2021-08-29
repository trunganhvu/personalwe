from django.db import models
from mainapp.model.Product import Product
from mainapp.model.Event import Event

class ProductPromotion(models.Model):
    """
    trunganhvu 2021/08/29
    """
    product_promotion_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    discount = models.IntegerField(default=0)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    product_promotion_start = models.DateField(null=False)
    product_promotion_end = models.DateField(null=False)
    created_at = models.DateField(null=False)
    updated_at = models.DateField(null=True)

    class Meta:
        app_label = "mainapp"