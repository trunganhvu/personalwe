from django.db import models

class BannerTitle(models.Model):
    """
    trunganhvu 2021/09/02
    """
    banner_title = models.CharField(max_length=60)
    banner_subtitle = models.CharField(max_length=120)
    display = models.BooleanField(default=False)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        app_label = "mainapp"
