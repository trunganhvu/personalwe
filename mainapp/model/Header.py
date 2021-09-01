from django.db import models

class Header(models.Model):
    """
    trunganhvu 2021/08/29
    """
    id = models.AutoField(primary_key=True)
    image_default_name = models.CharField(max_length=100)
    image_default_path = models.CharField(max_length=255)
    image_event_name = models.CharField(max_length=100, null=True)
    image_event_path = models.CharField(max_length=255, null=True)
    active = models.BooleanField(null=False, default=True)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        app_label = "mainapp"

