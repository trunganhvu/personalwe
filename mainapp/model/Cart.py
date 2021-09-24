from django.db import models

class Cart(models.Model):
    """
    trunganhvu 2021/09/24
    """
    cart_id = models.AutoField(primary_key=True)
    client_cookie_code = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(null=False, auto_now=True)


    class Meta:
        app_label = "mainapp"
