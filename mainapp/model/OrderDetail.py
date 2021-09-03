from django.db import models
from mainapp.model.Order import Order
from mainapp.model.ProductDetail import ProductDetail

class OrderDetail(models.Model):
    """
    trunganhvu 2021/08/29
    """
    order_detail_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_detail_id = models.ForeignKey(ProductDetail, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        app_label = "mainapp"