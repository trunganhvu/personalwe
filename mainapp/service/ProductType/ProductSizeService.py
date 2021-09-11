from django.core.cache import cache
from mainapp.Common import CacheUtil
from django.conf import settings

from mainapp.dao.ProductType import ProductSizeDao

KEY_CACHE_GET_ALL_PRODUCT_SIZE_IN_TYPE = 'context-all-product-size-in-type'
KEY_CACHE_GET_PRODUCT_SIZE_DETAIL_BY_ID = 'context-product-size-detail-in-'

def get_all_product_size_in_product_type(product_type_id):
    """
    Get all size in type
    """
    cached_data = cache.get(KEY_CACHE_GET_ALL_PRODUCT_SIZE_IN_TYPE)
    if not cached_data:
        # Get all in DB
        product_size_list = ProductSizeDao.get_all_product_size_in_product_type(product_type_id)

        if product_size_list.count() > 0:
            # Set into cache
            cache.set(KEY_CACHE_GET_ALL_PRODUCT_SIZE_IN_TYPE, product_size_list, settings.CACHE_TIME)
            cached_data = product_size_list 
    return cached_data

def get_product_size_detail_by_id(product_size_id):
    """
    Get product size detail by id
    """
    key_cache = KEY_CACHE_GET_PRODUCT_SIZE_DETAIL_BY_ID + str(product_size_id)
    cached_data = cache.get(key_cache)
    print(cached_data)
    if not cached_data:
        print('k cos cache')
        # Get detail in DB
        product_size = ProductSizeDao.get_product_size_detail_by_id(product_size_id)

        # Set into cache
        cache.set(key_cache, product_size, settings.CACHE_TIME)
        cached_data = product_size
    return cached_data

def insert_product_size(product_size):
    """
    Insert product size
    """
    # Insert into DB
    p_size = ProductSizeDao.insert_product_size(product_size)

    # Clean cache
    CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_PRODUCT_SIZE_IN_TYPE)

    key_cache = KEY_CACHE_GET_PRODUCT_SIZE_DETAIL_BY_ID + str(p_size.product_size_id)
    cache.set(key_cache, p_size, settings.CACHE_TIME)

def update_product_size(product_size):
    """
    Update product size
    """
    # Update into DB
    p_size = ProductSizeDao.update_product_size(product_size)
    print(p_size)
    # Clean cache
    CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_PRODUCT_SIZE_IN_TYPE)

    key_cache = KEY_CACHE_GET_PRODUCT_SIZE_DETAIL_BY_ID + str(p_size.product_size_id)
    CacheUtil.clean_cache_by_key(key_cache)
    
    cache.set(key_cache, p_size, settings.CACHE_TIME)

def delete_product_size_by_id(product_type_id):
    """
    Delete product size by id
    """
    p_size = get_product_size_detail_by_id(product_type_id)
    if p_size is not None:
        # Delete DB
        ProductSizeDao.delete_product_size_by_id(product_type_id)

        # Clean cache
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_PRODUCT_SIZE_IN_TYPE) 
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_PRODUCT_SIZE_DETAIL_BY_ID + str(product_type_id))