from mainapp.dao.Category import CategoryDao
from mainapp.Common import CacheUtil
from django.conf import settings
import imghdr
from django.core.cache import cache

KEY_CACHE_API_CATEGORY = 'context-api-category'

def get_all_category():
    """
    Get all category
    """
    cached_data = cache.get(KEY_CACHE_API_CATEGORY)
    if not cached_data:
        # Get category in DB
        category_list = CategoryDao.get_all_category()

        # Have category to return
        if category_list.count() > 0:
            # Set list category into cache
            cache.set(KEY_CACHE_API_CATEGORY, category_list, settings.CACHE_TIME)
            cached_data = category_list 
    return cached_data
