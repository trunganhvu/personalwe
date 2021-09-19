from django.core.cache import cache
from mainapp.Common import CacheUtil
from django.conf import settings

from mainapp.dao.Product import ProductPromotionDao
from mainapp.Common import Util

GET_ALL_PROMOTION_IS_RUNNING_IN_PRODUCT_ID = 'get-all-promotion-is-running-in-product-id-'
GET_ALL_PROMOTION_IS_COMING_IN_PRODUCT_ID = 'get-all-promotion-is-coming-in-product-id-'
GET_ALL_PROMOTION_IS_PASSED_IN_PRODUCT_ID = 'get-all-promotion-is-passed-in-product-id-'

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

def insert_product_promotion(product_promotion):
    """
    Insert promotion
    """

def update_product_promotion(product_promotion):
    """
    Update promotion
    """

def delete_product_promotion(product_promotion_id):
    """
    Delete product promotion by id
    """