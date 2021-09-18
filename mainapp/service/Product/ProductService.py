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
    p = ProductDao.update_product(product)

    # Set into cache
    # key_cache = KEY_CACHE_GET_PRODUCT_DETAIL_BY_ID + str(p.product_id)
    # CacheUtil.clean_cache_by_key(key_cache)
    # CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_PRODUCT_IN_TYPE + str(p.product_type_id_id))

    # cache.set(key_cache, p, settings.CACHE_TIME)
    return p

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

def update_product_and_detail(product, list_product_detail):
    """
    Update product and insert product detail
    """
    p = get_product_detail_by_id(product.product_id)
    if p is not None:
        list_p_detail = ProductDetailService.get_all_detail_product_by_product_id(product.product_id)
        # List id base
        list_p_detail_base_id = []
        for p_detail in list_p_detail:
            list_p_detail_base_id.append(int(p_detail.product_detail_id))
        
        # List id new
        list_p_detail_new_id = []
        for p_detail in list_product_detail:
            list_p_detail_new_id.append(int(p_detail.product_detail_id))

        # List id detail delete
        list_p_detail_delete = list(set(list_p_detail_base_id) - set(list_p_detail_new_id))

        # List id detail update
        list_p_detail_update = list(set(list_p_detail_base_id).intersection(list_p_detail_new_id))

        # List id detail insert
        list_p_detail_insert = list(set(list_p_detail_new_id) - set(list_p_detail_base_id))

        with transaction.atomic():
            # Update into table product
            p = update_product(product)

            # Insert or update into table detail
            for product_detail in list_product_detail:
                if int(product_detail.product_detail_id) in list_p_detail_update:                    
                    ProductDetailService.update_product_detail(product_detail)
                
                if int(product_detail.product_detail_id) in list_p_detail_insert:
                    product_detail.product_id = p
                    ProductDetailService.insert_product_detail(product_detail)

            # Delete detail
            for p_detail_id in list_p_detail_delete:
                ProductDetailService.delete_product_detail_by_pk(p_detail_id)

        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_PRODUCT_IN_TYPE + str(p.product_type_id_id))
        CacheUtil.clean_cache_by_key(ProductDetailService.KEY_CACHE_GET_PRODUCT_DETAIL_BY_ID + str(product.product_id))