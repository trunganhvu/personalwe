from django.core.cache import cache
from mainapp.Common import CacheUtil
from django.conf import settings

from mainapp.dao.Product import ProductDetailDao

KEY_CACHE_GET_PRODUCT_DETAIL_BY_ID = 'context-detail-product-detail-in-'
KEY_CACHE_GET_PRODUCT_DETAIL_BY_PRODUCT_DETAIL_ID = 'context-detail-product-detail-by-product-detail-id-'


def get_all_detail_product_by_product_id(product_id):
    """
    View detail by id
    """
    key_cache = KEY_CACHE_GET_PRODUCT_DETAIL_BY_ID + str(product_id)
    cached_data = cache.get(key_cache)
    if not cached_data:

        # Get detail color, size
        list_product_detail = ProductDetailDao.get_all_detail_product_by_product_id(product_id)

        # Set into cache
        cache.set(key_cache, list_product_detail, settings.CACHE_TIME)
        cached_data = list_product_detail 
    return cached_data

def get_product_detail_by_product_detail_id(product_detail_id):
    """
    View detail by id
    """
    key_cache = KEY_CACHE_GET_PRODUCT_DETAIL_BY_PRODUCT_DETAIL_ID + str(product_detail_id)
    cached_data = cache.get(key_cache)
    if not cached_data:

        # Get detail color, size
        list_product_detail = ProductDetailDao.get_all_detail_product_by_product_id(product_detail_id)

        # Set into cache
        cache.set(key_cache, list_product_detail, settings.CACHE_TIME)
        cached_data = list_product_detail 
    return cached_data

def delete_product_by_id(product_id):
    """
    Delete product by id
    """
    product = get_all_detail_product_by_product_id(product_id)
    if product is not None:
        # Delete in DB
        ProductDetailDao.delete_product_detail_by_product_id(product_id)

        # Delete cache
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_PRODUCT_DETAIL_BY_ID + str(product_id))

def insert_product_detail(product_detail):
    """
    Insert product detail
    """
    p_detail = ProductDetailDao.insert_product_detail(product_detail)

    # Set into cache
    # CacheUtil.clean_cache_by_key(KEY_CACHE_GET_PRODUCT_DETAIL_BY_ID + str(product_detail.product_id.product_id))

    # key_cache = KEY_CACHE_GET_PRODUCT_DETAIL_BY_ID + str(p_detail.product_type_id)
    # cache.set(key_cache, p_type, settings.CACHE_TIME)

def update_product_detail(product_detail):
    """
    Update product detail
    """
    p_detail = ProductDetailDao.update_product_detail(product_detail)

def delete_product_detail_by_pk(product_detail_id):
    """
    Delete product detail by product_detail_id
    """
    product_detail = get_product_detail_by_product_detail_id(product_detail_id)
    if product_detail is not None:
        # Delete in DB
        ProductDetailDao.delete_product_detail_by_pk(product_detail_id)

        # Delete cache
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_PRODUCT_DETAIL_BY_PRODUCT_DETAIL_ID + str(product_detail_id))