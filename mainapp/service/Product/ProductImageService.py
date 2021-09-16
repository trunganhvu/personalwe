from django.core.cache import cache
from mainapp.Common import CacheUtil
from django.conf import settings

from mainapp.dao.Product import ProductImageDao
from mainapp.Common import Util

KEY_CACHE_GET_PRODUCT_IMAGE_BY_ID = 'context-image-product-image-detail-by-'
KEY_CACHE_GET_ALL_PRODUCT_IMAGE_BY_PRODUCT_ID = 'context-image-get-all-product-image-by-product-id-'
KEY_CACHE_GET_PRODUCT_IMAGE_BY_IMAGE_ID = 'context-image-get-product-image-by-image-id-'


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

def insert_product_image(product_image):
    """
    Insert product image
    """
    full_path_image = ''
    try:
        # Save image
        full_path_image = Util.save_image_to_media(product_image.product_image_path,
                                                    product_image.product_image_name)
        product_image.product_image_path = full_path_image

        # Insert product image
        p_image = ProductImageDao.insert_image(product_image)

        key_cache_detail = KEY_CACHE_GET_PRODUCT_IMAGE_BY_IMAGE_ID + str(p_image.product_image_id)
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_PRODUCT_IMAGE_BY_PRODUCT_ID + str(p_image.product_id.product_id))

        cache.set(key_cache_detail, p_image, settings.CACHE_TIME)
    except Exception as error:
        if full_path_image == '':
            # Delete image
            Util.delete_image_in_media(full_path_image)
        raise error

def get_product_image_by_image_id(product_image_id):
    """
    Get product image by image id
    """
    key_cache = KEY_CACHE_GET_PRODUCT_IMAGE_BY_IMAGE_ID + str(product_image_id)
    cached_data = cache.get(key_cache)
    if not cached_data:
        # Get product image
        product_image = ProductImageDao.get_product_image_by_image_id(product_image_id)
    
        if product_image is not None:
            # Set into cache
            cache.set(key_cache, product_image, settings.CACHE_TIME)
            cached_data = product_image 
    return cached_data

def delete_product_image_by_image_id(product_id, product_image_id):
    """
    Delete product image by image id
    """
    product_image = get_product_image_by_image_id(product_image_id)
    if product_image is not None:
        # Delete in DB
        ProductImageDao.delete_image_by_id(product_image_id)

        # Delete cache
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_PRODUCT_IMAGE_BY_IMAGE_ID + str(product_image_id))
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_PRODUCT_IMAGE_BY_PRODUCT_ID + str(product_id))