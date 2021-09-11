from django.core.cache import cache
from mainapp.Common import CacheUtil
from django.conf import settings

from mainapp.dao.ProductType import ProductColorDao

KEY_CACHE_GET_ALL_PRODUCT_COLOR_IN_TYPE = 'context-all-product-color-in-type-'
KEY_CACHE_GET_PRODUCT_COLOR_DETAIL_BY_ID = 'context-product-color-detail-in-'

def get_all_product_color_in_type(product_type_id):
    """
    Get all product color
    """
    key_cache = KEY_CACHE_GET_ALL_PRODUCT_COLOR_IN_TYPE + str(product_type_id)
    cached_data = cache.get(key_cache)
    if not cached_data:
        # Get all in DB
        product_color_list = ProductColorDao.get_all_product_color_in_type(product_type_id)

        if product_color_list.count() > 0:
            # Set into cache
            cache.set(key_cache, product_color_list, settings.CACHE_TIME)
            cached_data = product_color_list 
    return cached_data

def get_product_color_detail_by_id(id):
    """
    View type detail by id
    """
    key_cache = KEY_CACHE_GET_PRODUCT_COLOR_DETAIL_BY_ID + str(id)
    cached_data = cache.get(key_cache)
    if not cached_data:
        # Get detail in DB
        product_color = ProductColorDao.get_product_color_detail_by_id(id)

        # Set into cache
        cache.set(key_cache, product_color, settings.CACHE_TIME)
        cached_data = product_color 
    return cached_data

def insert_product_color(product_color):
    """
    Insert type
    """
    # Insert into DB
    p_color = ProductColorDao.insert_product_color(product_color)

    # Set into cache
    CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_PRODUCT_COLOR_IN_TYPE + str(p_color.product_type_id))

    key_cache = KEY_CACHE_GET_PRODUCT_COLOR_DETAIL_BY_ID + str(p_color.product_color_id)
    cache.set(key_cache, p_color, settings.CACHE_TIME)

def update_product_color(product_color):
    """
    Update color
    """
    # Update to DB
    p_color = ProductColorDao.update_product_color(product_color)

    # Set into cache
    key_cache = KEY_CACHE_GET_PRODUCT_COLOR_DETAIL_BY_ID + str(p_color.product_color_id)
    CacheUtil.clean_cache_by_key(key_cache)
    CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_PRODUCT_COLOR_IN_TYPE + str(p_color.product_type_id))

    cache.set(key_cache, p_color, settings.CACHE_TIME)

def delete_product_color_by_id(id):
    """
    Delete color by id
    """
    product_color = get_product_color_detail_by_id(id)
    if product_color is not None:
        # Delete in DB
        ProductColorDao.delete_product_color_by_id(id)

        # Delete cache
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_PRODUCT_COLOR_DETAIL_BY_ID + str(id))
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_PRODUCT_COLOR_IN_TYPE + str(product_color.product_type_id))