from mainapp.model.Cart import Cart
from datetime import datetime
from django.core.cache import cache
from mainapp.Common import CacheUtil
from django.conf import settings
from django.utils import timezone

def get_cart_by_key_code(key_code):
    """
    Get cart by key code
    """
    cart_item = Cart.objects.filter(client_cookie_code=key_code).first()
    return cart_item

def insert_cart(client_cookie_code):
    """
    Insert cart
    """
    c = Cart(client_cookie_code=client_cookie_code)
    c.save()
    return c