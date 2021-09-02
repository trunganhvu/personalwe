from django.db import models

class Category(models.Model):
    """
    trunganhvu 2021/08/29
    """
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    category_url = models.CharField(max_length=100, unique=True)
    display = models.BooleanField(default=False)
    display_order = models.IntegerField(default=0)
    category_image_default_name = models.CharField(max_length=100)
    category_image_default = models.CharField(max_length=255)
    category_image_event_name = models.CharField(max_length=100, null=True)
    category_image_event = models.CharField(max_length=255, null=True)
    category_image_event_start = models.DateTimeField(null=True)
    category_image_event_end = models.DateTimeField(null=True)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        app_label = "mainapp"
