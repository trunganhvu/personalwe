from mainapp.model.BannerTitle import BannerTitle
from mainapp.Common import DateTime
from datetime import datetime

def get_banner_title():
    """
    Get banner title
    """
    banner_title = BannerTitle.objects.filter(display=True).first()
    print('dao')
    return banner_title

def update_banner_title(banner_title, banner_sub_title):
    """
    Update banner title
    """
    banner_title_db = BannerTitle.objects.filter(display=True).first()
    banner_title_db.banner_title = banner_title
    banner_title_db.banner_subtitle = banner_sub_title
    banner_title_db.save()

def insert_banner_title(banner_title, banner_sub_title):
    """
    Insert banner title
    """
    banner_title_db = BannerTitle(banner_title=banner_title, banner_subtitle=banner_sub_title, display=True)
    banner_title_db.save()

def count_banner_title_display():
    """
    Count banner title display
    """
    count_banner_title_display = BannerTitle.objects.filter(display=True).count()
    return count_banner_title_display