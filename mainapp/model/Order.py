from django.db import models
from mainapp.model.Delivery import Delivery

class Order(models.Model):
    """
    trunganhvu 2021/08/29
    """
    order_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=1000)
    order_code = models.CharField(max_length=1000)
    order_note = models.CharField(max_length=1000)
    order_time = models.DateTimeField(null=False)
    confirm_order_status = models.BooleanField(default=False)
    confirm_order_time = models.DateTimeField(null=True)
    delivery_id = models.ForeignKey(Delivery, on_delete=models.CASCADE)
    delivery_customer_pay = models.DecimalField(max_digits=12, decimal_places=2)
    delivery_shop_pay = models.DecimalField(max_digits=12, decimal_places=2)
    delivery_status = models.BooleanField(default=False)
    delivery_time = models.DateTimeField(null=True)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        app_label = "mainapp"