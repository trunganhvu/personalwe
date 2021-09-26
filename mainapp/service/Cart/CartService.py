from django.core.checks.messages import Error
from mainapp.Common import CacheUtil
from mainapp.dao.Cart import CartDao, CartDetailDao
from django.conf import settings

from django.core.cache import cache
from django.core.files.storage import FileSystemStorage
from django.db import transaction
from mainapp.model.CartDetail import CartDetail

COUNT_CART_ITEM_BY_KEY_CODE = 'count-cart-item-by-key-code-'
GET_CART_ITEM_BY_KEY_CODE = 'get-cart-item-by-key-code-'
GET_CART_BY_KEY_CODE = 'get-cart-by-key-code-'

def get_cart_by_key_code(key_code):
    """
    Get cart by cart id
    """
    cached_data = cache.get(GET_CART_BY_KEY_CODE + key_code)
    if not cached_data:
        # Get cart in DB
        cart = CartDao.get_cart_by_key_code(key_code)

        if cart is not None:
            cache.set(GET_CART_BY_KEY_CODE + key_code, cart, settings.CACHE_TIME)
            cached_data = cart 
    return cached_data

def count_cart_item_by_key_code(key_code):
    """
    Count cart item by key
    """
    cached_data = cache.get(COUNT_CART_ITEM_BY_KEY_CODE + key_code)
    if not cached_data:
        # Get cart in DB
        cart = get_cart_by_key_code(key_code)

        if cart is not None:
            count_cart_detail = CartDetailDao.count_cart_detail_by_cart_id(cart.cart_id)

            if int(count_cart_detail) > 0:
                context = {
                    'count': count_cart_detail
                }
                cache.set(COUNT_CART_ITEM_BY_KEY_CODE + key_code, context, settings.CACHE_TIME)
                cached_data = context 
    return cached_data

def get_cart_item_by_key_code(key_code):
    """
    Get cart item by key
    """
    cached_data = cache.get(GET_CART_ITEM_BY_KEY_CODE + str(key_code))
    if not cached_data:
        # Get cart in DB
        cart = get_cart_by_key_code(key_code)

        if cart is not None:
            list_cart_detail = CartDetailDao.get_cart_detail_by_cart_id(cart.cart_id)

            if list_cart_detail.count() > 0:
                cache.set(GET_CART_ITEM_BY_KEY_CODE + str(key_code), list_cart_detail, settings.CACHE_TIME)
                cached_data = list_cart_detail 
    return cached_data

def insert_cart(key_code):
    """
    Insert new cart
    """
    cart = CartDao.insert_cart(key_code)
    return cart

def insert_cart_and_item(product_detail_id, cart_quantity, cart_cookie_key):
    """
    Insert cart and item
    """
    # Get cart
    c = get_cart_by_key_code(cart_cookie_key)

    # If not cart
    if c is None:
        # Insert all
        with transaction.atomic():
            # insert cart
            cart = insert_cart(cart_cookie_key)

            # insert cart detail
            cart_detail = CartDetail(cart_id=cart,
                                    product_detail_id_id=product_detail_id,
                                    quantity=cart_quantity)
            c_detail = CartDetailDao.insert_cart_detail(cart_detail)
    else:
        # Insert cart detail
        # Check detail exist
        c_detail = CartDetailDao.get_cart_detail_by_pk_product_detail_id(c.cart_id, product_detail_id)

        # Insert
        if c_detail is None:
            cart_detail = CartDetail(cart_id=c,
                                    product_detail_id_id=product_detail_id,
                                    quantity=cart_quantity)
            c_detail_new = CartDetailDao.insert_cart_detail(cart_detail)
            CacheUtil.clean_cache_by_key(COUNT_CART_ITEM_BY_KEY_CODE + cart_cookie_key)
            CacheUtil.clean_cache_by_key(GET_CART_ITEM_BY_KEY_CODE + cart_cookie_key)

        else:
            # Update quantity
            quatity_update = int(cart_quantity) + int(c_detail.quantity)
            print(quatity_update)
            print(type(quatity_update))
            print(c_detail.cart_detail_id)
            c_detail_new = CartDetailDao.update_cart_detail(c_detail.cart_detail_id, quatity_update)
            CacheUtil.clean_cache_by_key(GET_CART_ITEM_BY_KEY_CODE + cart_cookie_key)

def update_quantity_cart_detail(cart_detail_id, quantity, cart_cookie_key):
    """
    Update quantity detail
    """
    print(quantity)
    CartDetailDao.update_cart_detail(cart_detail_id, quantity)
    CacheUtil.clean_cache_by_key(GET_CART_ITEM_BY_KEY_CODE + cart_cookie_key)
