from mainapp.model.Category import Category
from mainapp.dao.Category import CategoryDao
from mainapp.Common import CacheUtil
from django.conf import settings
import imghdr
from django.core.cache import cache
from django.core.files.storage import FileSystemStorage
import os

KEY_CACHE_API_CATEGORY = 'context-api-category'
KEY_CACHE_API_CATEGORY_ID = 'context-api-category-id-'
KEY_CACHE_API_CATEGORY_DISPLAY = 'context-api-category-display'
def get_all_category():
    """
    Get all category
    """
    cached_data = cache.get(KEY_CACHE_API_CATEGORY)
    if not cached_data:
        # Get category in DB
        category_list = CategoryDao.get_all_category()

        # Have category to return
        if category_list.count() > 0:
            # Set list category into cache
            cache.set(KEY_CACHE_API_CATEGORY, category_list, settings.CACHE_TIME)
            cached_data = category_list 
    return cached_data

def insert_category(category_name, category_url, category_image_name, category_image, category_display, category_display_order):
    """
    Insert category
    """
    full_path_image = ''
    try:
        # Set image name saved
        image_name_save = category_image_name + '.' + str(imghdr.what(category_image))
        # Dir save
        fs = FileSystemStorage(location=settings.IMAGE_USER)
        # Save image
        filename = fs.save(image_name_save, category_image)
        # Url dir save
        uploaded_file_url = fs.url(filename)
        full_path_image = settings.IMAGE_PATH_STATIC + uploaded_file_url
        
        # Change display
        category_display = True if category_display == 'true' else False

        # Change display order
        category_display_order = 0 if category_display_order == '' else category_display_order

        # Insert to DB
        category = CategoryDao.insert_category(category_name, category_url, category_image_name, full_path_image, category_display, category_display_order)
        
        # Clean cache
        CacheUtil.clean_cache_by_key(KEY_CACHE_API_CATEGORY)

        # Set category into cache
        key_cache = str(KEY_CACHE_API_CATEGORY_ID) + str(category.category_id)
        cache.set(key_cache, category, settings.CACHE_TIME)
    except Exception as error: 
        if full_path_image != '':
            path1 = str(settings.BASE_DIR) + '/' + settings.APP_NAME1 + '/' + full_path_image
            path2 = str(settings.BASE_DIR) + '/' + full_path_image
            os.remove(path1)
            os.remove(path2)
        raise error

def get_category_detail(id):
    """
    Get category detail
    """
    key_cache = str(KEY_CACHE_API_CATEGORY_ID) + str(id)
    cached_data = cache.get(key_cache)
    if not cached_data:
        print('Khong co cache')
        # Get category in DB
        category = CategoryDao.get_category_detail(id)

        # Set list category into cache
        cache.set(key_cache, category, settings.CACHE_TIME)
        cached_data = category 
    return cached_data

def update_category(category, is_update_image):
    """
    Update category
    """
    full_path_image = ''
    try:
        # If have new image
        if is_update_image:
            image_name_save = category.category_image_default_name + '.' + str(imghdr.what(category.category_image_default))
            # Dir save
            fs = FileSystemStorage(location=settings.IMAGE_USER)
            # Save image
            filename = fs.save(image_name_save, category.category_image_default)
            # Url dir save
            uploaded_file_url = fs.url(filename)
            full_path_image = settings.IMAGE_PATH_STATIC + uploaded_file_url
            
            category.category_image_default = full_path_image
        print('path:' + category.category_image_default)
        # Change display
        category.display = True if category.display == 'true' else False

        # Update to DB
        category_updated = CategoryDao.update_category(category)

        # Clean cache
        CacheUtil.clean_cache_by_key(KEY_CACHE_API_CATEGORY)
        CacheUtil.clean_cache_by_key(KEY_CACHE_API_CATEGORY_DISPLAY)

        # Reset category into cache
        key_cache = str(KEY_CACHE_API_CATEGORY_ID) + str(category_updated.category_id)
        cache.set(key_cache, category_updated, settings.CACHE_TIME)
    except Exception as error:
        if full_path_image != '':
            path1 = str(settings.BASE_DIR) + '/' + settings.APP_NAME1 + '/' + full_path_image
            path2 = str(settings.BASE_DIR) + '/' + full_path_image
            os.remove(path1)
            os.remove(path2)
        raise error

def get_category_display():
    """
    Get all category display
    """
    cached_data = cache.get(KEY_CACHE_API_CATEGORY_DISPLAY)
    if not cached_data:
        print('Khong co cache')

        # Get category in DB
        category_list = CategoryDao.get_category_display()

        # Have category to return
        if category_list.count() > 0:
            # Set list category into cache
            cache.set(KEY_CACHE_API_CATEGORY_DISPLAY, category_list, settings.CACHE_TIME)
            cached_data = category_list 
    return cached_data