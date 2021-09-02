from django.core.cache import cache

def clean_cache_by_key(key):
    """
    Clean cache by key
    """
    cache.delete(key)