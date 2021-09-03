from django.db import models

class Delivery(models.Model):
    """
    trunganhvu 2021/08/29
    """
    delivery_id = models.AutoField(primary_key=True)
    delivery_name = models.CharField(max_length=100)
    delivery_phone =  models.CharField(max_length=25)
    delivery_price = models.DecimalField(max_digits=12, decimal_places=2)
    is_using = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        app_label = "mainapp"