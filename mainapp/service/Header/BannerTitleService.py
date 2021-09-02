from mainapp.dao.Header import BannerTitleDao
from mainapp.Common import CacheUtil
from django.conf import settings
import imghdr
from django.core.cache import cache

KEY_CACHE_API_BANNER_TITLE = 'context-api-banner-title'

def get_banner_title():
    """
    Get banner title
    """
    # Check data title in cache
    cached_data = cache.get(KEY_CACHE_API_BANNER_TITLE)
    if not cached_data:
        # Get banner title in DB
        banner_title = BannerTitleDao.get_banner_title()
        # Have title to return
        if banner_title is not None:
            context = {
                'bannerTitle': banner_title.banner_title,
                'bannerSubTitle': banner_title.banner_subtitle,
                'updatedAt': banner_title.updated_at
            }
            # Set banner title into cache
            cache.set(KEY_CACHE_API_BANNER_TITLE, context, settings.CACHE_TIME)
        else:
            context = {
                'bannerTitle': None,
                'bannerSubTitle': None
            }
        cached_data = context 
    return cached_data

def update_banner_title(banner_title, banner_sub_title):
    """
    Update banner title
    """
    try:
        count_banner_title_display = BannerTitleDao.count_banner_title_display()
        if count_banner_title_display == 0:
            BannerTitleDao.insert_banner_title(banner_title, banner_sub_title)
        else:
            BannerTitleDao.update_banner_title(banner_title, banner_sub_title)
        # Clean cache header
        CacheUtil.clean_cache_by_key(KEY_CACHE_API_BANNER_TITLE)
    except Exception as error: 
        raise error
