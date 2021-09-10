from django import db
from mainapp.dao.ProductType import ProductTypeDao
from django.core.cache import cache
from mainapp.Common import CacheUtil
from django.conf import settings

KEY_CACHE_GET_ALL_PRODUCT_TYPE = 'context-all-product-type'
KEY_CACHE_GET_PRODUCT_TYPE_DETAIL_BY_ID = 'context-product-type-detail-id-'


def get_all_product_type():
    """
    Get all product type
    """
    cached_data = cache.get(KEY_CACHE_GET_ALL_PRODUCT_TYPE)
    if not cached_data:
        # Get all in DB
        product_type_list = ProductTypeDao.get_all_product_type()

        if product_type_list.count() > 0:
            # Set into cache
            cache.set(KEY_CACHE_GET_ALL_PRODUCT_TYPE, product_type_list, settings.CACHE_TIME)
            cached_data = product_type_list 
    return cached_data

def get_product_type_detail_by_id(id):
    """
    View type detail by id
    """
    key_cache = KEY_CACHE_GET_PRODUCT_TYPE_DETAIL_BY_ID + str(id)
    cached_data = cache.get(key_cache)
    if not cached_data:
        # Get detail in DB
        product_type = ProductTypeDao.view_product_type_detail_by_id(id)

        # Set into cache
        cache.set(key_cache, product_type, settings.CACHE_TIME)
        cached_data = product_type 
    return cached_data

def insert_product_type(product_type):
    """
    Insert type
    """
    # Insert into DB
    p_type = ProductTypeDao.insert_product_type(product_type)

    # Set into cache
    key_cache = KEY_CACHE_GET_PRODUCT_TYPE_DETAIL_BY_ID + str(p_type.product_type_id)
    cache.set(key_cache, product_type, settings.CACHE_TIME)

def update_product_type(product_type):
    """
    Update type
    """
    # Update to DB
    p_type = ProductTypeDao.update_product_type(product_type)

    # Set into cache
    key_cache = KEY_CACHE_GET_PRODUCT_TYPE_DETAIL_BY_ID + str(p_type.product_type_id)
    CacheUtil.clean_cache_by_key(key_cache)
    cache.set(key_cache, product_type, settings.CACHE_TIME)

def delete_product_type_by_id(id):
    """
    Delete type by id
    """
    product_type = get_product_type_detail_by_id(id)
    if product_type is not None:
        ProductTypeDao.delete_product_type_by_id(id)

        # Delete cache
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_PRODUCT_TYPE_DETAIL_BY_ID + str(id))
