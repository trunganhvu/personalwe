from django.core.checks.messages import Error
from mainapp.Common import CacheUtil
from mainapp.dao.Category import CategoryPostDao
from django.conf import settings
import imghdr
from django.core.cache import cache
from django.core.files.storage import FileSystemStorage
import os

KEY_CACHE_API_CATEGORY_POST = 'context-api-category-post'
KEY_CACHE_API_CATEGORY_POST_IN_CATEGORY = 'context-api-category-post-in-categoy-'
KEY_CACHE_API_CATEGORY_POST_ID = 'context-api-category-post-id-'
KEY_CACHE_API_CATEGORY_POST_DISPLAY = 'context-api-category-post-display'
KEY_CACHE_CATEGORY_POST_DISPLAY_IN_CATEGORY = 'context-api-category-post-display-in-categoy-'
KEY_CACHE_CATEGORY_POST_DETAIL_DISPLAY_BY_URL = 'context-api-category-post-detail-display-by-url-'
KEY_CACHE_CATEGORY_POST_DISPLAY_LIMIT_IN_CATEGORY = 'context-category-post-display-limit-in-categoy-'

def get_all_category_post():
    """
    Get all post
    """
    cached_data = cache.get(KEY_CACHE_API_CATEGORY_POST)
    if not cached_data:
        # Get post in DB
        post_list = CategoryPostDao.get_all_category_post()

        # Have post to return
        if post_list.count() > 0:
            # Set list post into cache
            cache.set(KEY_CACHE_API_CATEGORY_POST, post_list, settings.CACHE_TIME)
            cached_data = post_list 
    return cached_data

def get_all_post_in_category(id):
    """
    Get all post in category by category_id
    """
    key_cache = str(KEY_CACHE_API_CATEGORY_POST_IN_CATEGORY) + str(id)
    cached_data = cache.get(key_cache)
    if not cached_data:
        # Get post in DB
        post_list = CategoryPostDao.get_all_post_by_category_id(id)
        # Have post to return
        if post_list.count() > 0:
            # Set list post into cache
            cache.set(key_cache, post_list, settings.CACHE_TIME)
            cached_data = post_list
        else:
            cached_data = {}
    return cached_data

def get_all_post_display_in_category(id):
    """
    Get all post display in category
    """
    key_cache = str(KEY_CACHE_CATEGORY_POST_DISPLAY_IN_CATEGORY) + str(id)
    cached_data = cache.get(key_cache)
    if not cached_data:
        # Get post in DB
        post_list = CategoryPostDao.get_all_post_display_by_category_id(id)
        # Have post to return
        if post_list.count() > 0:
            # Set list post into cache
            cache.set(key_cache, post_list, settings.CACHE_TIME)
            cached_data = post_list
        else:
            cached_data = {}
    return cached_data

def get_limit_post_display_in_category(id):
    """
    Get post display in category (limit record)
    """
    key_cache = str(KEY_CACHE_CATEGORY_POST_DISPLAY_LIMIT_IN_CATEGORY) + str(id)
    cached_data = cache.get(key_cache)
    if not cached_data:
        # Get post in DB
        post_list = CategoryPostDao.get_limit_post_display_by_category_id(id)
        # Have post to return
        if post_list.count() > 0:
            # Set list post into cache
            cache.set(key_cache, post_list, settings.CACHE_TIME)
            cached_data = post_list
        else:
            cached_data = {}
    return cached_data

def get_detail_post_by_id(id):
    """
    Get detail post by id
    """
    cached_data = cache.get(KEY_CACHE_API_CATEGORY_POST_ID + str(id))
    if not cached_data:
        # Get post in DB
        post = CategoryPostDao.get_post_detail_by_id(id)

        # Set list post into cache
        cache.set(KEY_CACHE_API_CATEGORY_POST_ID + str(id), post, settings.CACHE_TIME)
        cached_data = post 
    return cached_data

def get_detail_post_public_by_url(url):
    """
    Get detail post public by url
    """
    cached_data = cache.get(KEY_CACHE_CATEGORY_POST_DETAIL_DISPLAY_BY_URL + url)
    if not cached_data:
        # Get post in DB
        post = CategoryPostDao.get_post_detail_display_by_url(url)

        # Set list post into cache
        cache.set(KEY_CACHE_CATEGORY_POST_DETAIL_DISPLAY_BY_URL + url, post, settings.CACHE_TIME)
        cached_data = post 
    return cached_data

def insert_post(post):
    """
    Insert new category post
    """
    full_path_image = ''
    try:
        # Set image name saved
        image_name_save = post.category_post_image_name + '.' + str(imghdr.what(post.category_post_image))
        # Dir save
        fs = FileSystemStorage(location=settings.IMAGE_USER)
        # Save image
        filename = fs.save(image_name_save, post.category_post_image)
        # Url dir save
        uploaded_file_url = fs.url(filename)
        full_path_image = settings.IMAGE_PATH_STATIC + uploaded_file_url

        post.category_post_image = full_path_image

        # Change display
        post.display = True if post.display == 'true' else False

        # Change display order
        post.display_order = 0 if post.display_order == '' else post.display_order

        # Save into DB
        category_post = CategoryPostDao.insert_category_post(post)

        # Clean cache list
        CacheUtil.clean_cache_by_key(KEY_CACHE_API_CATEGORY_POST)
        CacheUtil.clean_cache_by_key(str(KEY_CACHE_API_CATEGORY_POST_IN_CATEGORY) + str(post.category_id_id))
        CacheUtil.clean_cache_by_key(str(KEY_CACHE_CATEGORY_POST_DISPLAY_IN_CATEGORY) + str(category_post.category_id_id))
        CacheUtil.clean_cache_by_key(KEY_CACHE_CATEGORY_POST_DETAIL_DISPLAY_BY_URL + str(category_post.category_post_url))
        CacheUtil.clean_cache_by_key(KEY_CACHE_CATEGORY_POST_DISPLAY_LIMIT_IN_CATEGORY + str(category_post.category_id_id))
        
        # Save cache
        key_cache = str(KEY_CACHE_API_CATEGORY_POST_ID) + str(category_post.category_post_id)
        cache.set(key_cache, category_post, settings.CACHE_TIME)
    except Exception as error:
        if full_path_image != '':
            path1 = str(settings.BASE_DIR) + '/' + settings.APP_NAME1 + '/' + full_path_image
            path2 = str(settings.BASE_DIR) + '/' + full_path_image
            os.remove(path1)
            os.remove(path2)
        print('error: ' + str(error))
        raise error

def update_post(post, is_update_image):
    """
    Update new category post
    """
    full_path_image = ''
    try:
        if is_update_image:
            # Set image name saved
            image_name_save = post.category_post_image_name + '.' + str(imghdr.what(post.category_post_image))
            # Dir save
            fs = FileSystemStorage(location=settings.IMAGE_USER)
            # Save image
            filename = fs.save(image_name_save, post.category_post_image)
            # Url dir save
            uploaded_file_url = fs.url(filename)
            full_path_image = settings.IMAGE_PATH_STATIC + uploaded_file_url

            post.category_post_image = full_path_image

        # Change display
        post.display = True if post.display == 'true' else False

        # Change display order
        post.display_order = 0 if post.display_order == '' else post.display_order

        # Save vao DB
        category_post = CategoryPostDao.update_category_post(post)

        # Clean cache list
        CacheUtil.clean_cache_by_key(KEY_CACHE_API_CATEGORY_POST)
        CacheUtil.clean_cache_by_key(str(KEY_CACHE_API_CATEGORY_POST_IN_CATEGORY) + str(post.category_id_id))
        CacheUtil.clean_cache_by_key(str(KEY_CACHE_CATEGORY_POST_DISPLAY_IN_CATEGORY) + str(category_post.category_id_id))
        CacheUtil.clean_cache_by_key(KEY_CACHE_CATEGORY_POST_DETAIL_DISPLAY_BY_URL + str(category_post.category_post_url))
        CacheUtil.clean_cache_by_key(KEY_CACHE_CATEGORY_POST_DISPLAY_LIMIT_IN_CATEGORY + str(category_post.category_id_id))

        # Reset cache
        key_cache = str(KEY_CACHE_API_CATEGORY_POST_ID) + str(category_post.category_post_id)
        CacheUtil.clean_cache_by_key(key_cache)
        cache.set(key_cache, category_post, settings.CACHE_TIME)
    except Exception as error:
        if full_path_image != '':
            path1 = str(settings.BASE_DIR) + '/' + settings.APP_NAME1 + '/' + full_path_image
            path2 = str(settings.BASE_DIR) + '/' + full_path_image
            os.remove(path1)
            os.remove(path2)
        print('error: ' + str(error))
        raise error