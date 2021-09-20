from django.core.cache import cache
from mainapp.Common import CacheUtil
from django.conf import settings

from mainapp.dao.Product import ProductPromotionDao
from mainapp.Common import Util

GET_ALL_PROMOTION_IS_RUNNING_IN_PRODUCT_ID = 'get-all-promotion-is-running-in-product-id-'
GET_ALL_PROMOTION_IS_COMING_IN_PRODUCT_ID = 'get-all-promotion-is-coming-in-product-id-'
GET_ALL_PROMOTION_IS_PASSED_IN_PRODUCT_ID = 'get-all-promotion-is-passed-in-product-id-'
GET_PROMOTION_DETAIL_BY_PROMOTION_ID = 'get-promotion-detail-by-promotion-id-'


def get_all_promotion_is_running_in_product_id(product_id):
    """
    Get all promotion is running in product id
    """
    key_cache = GET_ALL_PROMOTION_IS_RUNNING_IN_PRODUCT_ID + str(product_id)
    cached_data = cache.get(key_cache)
    if not cached_data:

        # Get detail color, size
        list_product_promotion = ProductPromotionDao.get_all_promotion_active_in_product(product_id)

        # Set into cache
        cache.set(key_cache, list_product_promotion, settings.CACHE_TIME)
        cached_data = list_product_promotion 
    return cached_data

def get_all_promotion_is_coming_in_product_id(product_id):
    """
    Get all promotion is coming in product
    """
    key_cache = GET_ALL_PROMOTION_IS_COMING_IN_PRODUCT_ID + str(product_id)
    cached_data = cache.get(key_cache)
    if not cached_data:
        # Get detail color, size
        list_product_promotion = ProductPromotionDao.get_all_promotion_is_coming_in_product_id(product_id)

        # Set into cache
        cache.set(key_cache, list_product_promotion, settings.CACHE_TIME)
        cached_data = list_product_promotion 
    return cached_data
    
def get_all_promotion_is_passed_in_product_id(product_id):
    """
    Get all promotion is passed in product
    """
    key_cache = GET_ALL_PROMOTION_IS_PASSED_IN_PRODUCT_ID + str(product_id)
    cached_data = cache.get(key_cache)
    if not cached_data:
        # Get detail color, size
        list_product_promotion = ProductPromotionDao.get_all_promotion_is_passed_in_product_id(product_id)

        # Set into cache
        cache.set(key_cache, list_product_promotion, settings.CACHE_TIME)
        cached_data = list_product_promotion 
    return cached_data

def get_product_promotion_detail_by_promotion_id(product_promotion_id):
    """
    Get product promotion detail by id
    """
    key_cache = GET_PROMOTION_DETAIL_BY_PROMOTION_ID + str(product_promotion_id)
    cached_data = cache.get(key_cache)
    if not cached_data:
        # Get detail color, size
        product_promotion = ProductPromotionDao.get_promotion_detail_by_promotion_id(product_promotion_id)

        # Set into cache
        cache.set(key_cache, product_promotion, settings.CACHE_TIME)
        cached_data = product_promotion 
    return cached_data

def insert_product_promotion(product_promotion):
    """
    Insert promotion
    """
    # Insert 
    p_promotion = ProductPromotionDao.insert_promotion(product_promotion)

    # Clean cache
    CacheUtil.clean_cache_by_key(GET_ALL_PROMOTION_IS_RUNNING_IN_PRODUCT_ID + str(p_promotion.product_id.product_id))
    CacheUtil.clean_cache_by_key(GET_ALL_PROMOTION_IS_COMING_IN_PRODUCT_ID + str(p_promotion.product_id.product_id))
    CacheUtil.clean_cache_by_key(GET_ALL_PROMOTION_IS_PASSED_IN_PRODUCT_ID + str(p_promotion.product_id.product_id))


def update_product_promotion(product_promotion):
    """
    Update promotion
    """
    if int(product_promotion.event_id_id) == 0:
        product_promotion.event_id_id = None
    
    p_promotion = ProductPromotionDao.update_promotion(product_promotion)

    # Clean cache
    CacheUtil.clean_cache_by_key(GET_PROMOTION_DETAIL_BY_PROMOTION_ID + str(p_promotion.product_promotion_id))
    CacheUtil.clean_cache_by_key(GET_ALL_PROMOTION_IS_RUNNING_IN_PRODUCT_ID + str(p_promotion.product_id.product_id))
    CacheUtil.clean_cache_by_key(GET_ALL_PROMOTION_IS_COMING_IN_PRODUCT_ID + str(p_promotion.product_id.product_id))
    CacheUtil.clean_cache_by_key(GET_ALL_PROMOTION_IS_PASSED_IN_PRODUCT_ID + str(p_promotion.product_id.product_id))

def delete_product_promotion(product_promotion_id):
    """
    Delete product promotion by id
    """
    p_promotion = get_product_promotion_detail_by_promotion_id(product_promotion_id)
    if p_promotion is not None:
        ProductPromotionDao.delete_promotion(p_promotion.product_promotion_id)

        # Clean cache
        CacheUtil.clean_cache_by_key(GET_PROMOTION_DETAIL_BY_PROMOTION_ID + str(p_promotion.product_promotion_id))
        CacheUtil.clean_cache_by_key(GET_ALL_PROMOTION_IS_RUNNING_IN_PRODUCT_ID + str(p_promotion.product_id.product_id))
        CacheUtil.clean_cache_by_key(GET_ALL_PROMOTION_IS_COMING_IN_PRODUCT_ID + str(p_promotion.product_id.product_id))
        CacheUtil.clean_cache_by_key(GET_ALL_PROMOTION_IS_PASSED_IN_PRODUCT_ID + str(p_promotion.product_id.product_id))

