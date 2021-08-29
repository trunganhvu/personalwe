from django.db import models

class Event(models.Model):
    """
    trunganhvu 2021/08/29
    """
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=255)
    event_note = models.CharField(max_length=1000)
    event_slogun = models.CharField(max_length=500)
    event_description = models.CharField(max_length=1000)
    event_image_banner = models.CharField(max_length=255)
    active = models.BooleanField(default=False)
    event_start = models.DateField(null=True)
    event_end = models.DateField(null=True)
    created_at = models.DateField(null=False)
    updated_at = models.DateField(null=True)

    class Meta:
        app_label = "mainapp"