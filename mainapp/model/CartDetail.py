from django.db import models
from mainapp.model.Cart import Cart
from mainapp.model.ProductDetail import ProductDetail

class CartDetail(models.Model):
    """
    trunganhvu 2021/09/24
    """
    cart_detail_id = models.AutoField(primary_key=True)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product_detail_id = models.ForeignKey(ProductDetail, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)
    updated_at = models.DateTimeField(null=False, auto_now=True)

    class Meta:
        app_label = "mainapp"
