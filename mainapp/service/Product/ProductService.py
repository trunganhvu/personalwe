from django.core.cache import cache
from mainapp.Common import CacheUtil
from django.conf import settings
from django.db import transaction
from mainapp.dao.Product import ProductDao
from mainapp.service.Product import ProductDetailService
KEY_CACHE_GET_ALL_PRODUCT_IN_TYPE = 'context-all-product-in-type-'
KEY_CACHE_GET_PRODUCT_DETAIL_BY_ID = 'context-product-detail-in-'

def get_all_product_in_type(product_type_id):
    """
    Get all product 
    """
    key_cache = KEY_CACHE_GET_ALL_PRODUCT_IN_TYPE + str(product_type_id)
    cached_data = cache.get(key_cache)
    if not cached_data:
        # Get all in DB
        product_list = ProductDao.get_all_product_in_type(product_type_id)

        if product_list.count() > 0:
            # Set into cache
            cache.set(key_cache, product_list, settings.CACHE_TIME)
            cached_data = product_list 
    return cached_data

def get_product_detail_by_id(id):
    """
    View detail by id
    """
    key_cache = KEY_CACHE_GET_PRODUCT_DETAIL_BY_ID + str(id)
    cached_data = cache.get(key_cache)
    if not cached_data:
        # Get detail in DB
        product = ProductDao.get_product_detail_by_id(id)
        
        # Set into cache
        cache.set(key_cache, product, settings.CACHE_TIME)
        cached_data = product 
    return cached_data

def insert_product(product):
    """
    Insert product
    """
    # Insert into DB
    p = ProductDao.insert_product(product)

    # Set into cache
    # CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_PRODUCT_IN_TYPE + str(p.product_type_id_id))

    # key_cache = KEY_CACHE_GET_PRODUCT_DETAIL_BY_ID + str(p.product_id)
    # cache.set(key_cache, p, settings.CACHE_TIME)
    return p

def update_product(product):
    """
    Update product
    """
    # Update to DB
    p = ProductDao.update_product_(product)

    # Set into cache
    key_cache = KEY_CACHE_GET_PRODUCT_DETAIL_BY_ID + str(p.product_id)
    CacheUtil.clean_cache_by_key(key_cache)
    CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_PRODUCT_IN_TYPE + str(p.product_type_id_id))

    cache.set(key_cache, p, settings.CACHE_TIME)

def delete_product_by_id(id):
    """
    Delete product by id
    """
    product = get_product_detail_by_id(id)
    if product is not None:
        # Delete in DB
        ProductDao.delete_product(id)

        # Delete cache
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_PRODUCT_DETAIL_BY_ID + str(id))
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_PRODUCT_IN_TYPE + str(product.product_type_id_id))

def insert_product_and_detail(product, list_product_detail):
    """
    Insert product and insert product detail
    """
    # pro = ProductDao.insert_product_and_detail(product, list_product_detail)
    with transaction.atomic():
        # Insert into table product
        p = insert_product(product)

        # Insert into table detail
        for product_detail in list_product_detail:
            product_detail.product_id = p
            ProductDetailService.insert_product_detail(product_detail)
    CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_PRODUCT_IN_TYPE + str(p.product_type_id_id))