from django.core.checks.messages import Error
from mainapp.Common import CacheUtil
from mainapp.dao.Cart import CartDao, CartDetailDao
from django.conf import settings
import imghdr
from django.core.cache import cache
from django.core.files.storage import FileSystemStorage
import os

COUNT_CART_ITEM_BY_KEY_CODE = 'count-cart-item-by-key-code-'
GET_CART_ITEM_BY_KEY_CODE = 'get-cart-item-by-key-code-'
GET_CART_BY_KEY_CODE = 'get-cart-by-key-code-'

def get_cart_by_key_code(key_code):
    """
    Get cart by cart id
    """
    cached_data = cache.get(GET_CART_BY_KEY_CODE)
    if not cached_data:
        # Get cart in DB
        cart = CartDao.get_cart_by_key_code(key_code)

        if cart is not None:
            cache.set(GET_CART_BY_KEY_CODE, key_code, settings.CACHE_TIME)
            cached_data = cart 
    return cached_data

def count_cart_item_by_key_code(key_code):
    """
    Count cart item by key
    """
    cached_data = cache.get(COUNT_CART_ITEM_BY_KEY_CODE)
    if not cached_data:
        # Get cart in DB
        cart = get_cart_by_key_code(key_code)
        print(cart)

        if cart is not None:
            count_cart_detail = CartDetailDao.count_cart_detail_by_cart_id(cart.cart_id)
            print(count_cart_detail)
            if int(count_cart_detail) > 0:
                context = {
                    'count': count_cart_detail
                }
                cache.set(COUNT_CART_ITEM_BY_KEY_CODE, context, settings.CACHE_TIME)
                cached_data = context 
    return cached_data

def get_cart_item_by_key_code(key_code):
    """
    Get cart item by key
    """
    cached_data = cache.get(GET_CART_ITEM_BY_KEY_CODE)
    if not cached_data:
        # Get cart in DB
        cart = get_cart_by_key_code(key_code)

        if cart is not None:
            list_cart_detail = CartDetailDao.get_cart_detail_by_cart_id(cart.cart_id)

            if list_cart_detail.count() > 0:
                cache.set(GET_CART_ITEM_BY_KEY_CODE, list_cart_detail, settings.CACHE_TIME)
                cached_data = list_cart_detail 
    return cached_data