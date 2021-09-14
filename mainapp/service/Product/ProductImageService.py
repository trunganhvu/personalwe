from django.core.cache import cache
from mainapp.Common import CacheUtil
from django.conf import settings

from mainapp.dao.Product import ProductImageDao

KEY_CACHE_GET_PRODUCT_IMAGE_BY_ID = 'context-image-product-image-detail-by-'
KEY_CACHE_GET_ALL_PRODUCT_IMAGE_BY_PRODUCT_ID = 'context-image-get-all-product-image-by-product-id-'


def get_all_product_image_by_product_id(product_id):
    """
    Get all image product by product id
    """
    key_cache = KEY_CACHE_GET_ALL_PRODUCT_IMAGE_BY_PRODUCT_ID + str(product_id)
    cached_data = cache.get(key_cache)
    if not cached_data:

        # Get image
        list_product_detail = ProductImageDao.get_all_image_in_product(product_id)

        # Set into cache
        cache.set(key_cache, list_product_detail, settings.CACHE_TIME)
        cached_data = list_product_detail 
    return cached_data

def delete_all_product_image_by_product_id(product_id):
    """
    Delete product image by product id
    """
    product_images = get_all_product_image_by_product_id(product_id)
    if product_images is not None:
        # Delete in DB
        ProductImageDao.delete_all_product_image_by_product_id(product_id)

        # Delete cache
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_PRODUCT_IMAGE_BY_PRODUCT_ID + str(product_id))