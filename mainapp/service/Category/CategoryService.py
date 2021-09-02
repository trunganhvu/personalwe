from mainapp.model.Category import Category
from mainapp.dao.Category import CategoryDao
from mainapp.Common import CacheUtil
from django.conf import settings
import imghdr
from django.core.cache import cache
from django.core.files.storage import FileSystemStorage
import os

KEY_CACHE_API_CATEGORY = 'context-api-category'

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
        # Insert to DB
        CategoryDao.insert_category(category_name, category_url, category_image_name, full_path_image, category_display, category_display_order)

    except Exception as error: 
        if full_path_image != '':
            path1 = str(settings.BASE_DIR) + '/' + settings.APP_NAME1 + '/' + full_path_image
            path2 = str(settings.BASE_DIR) + '/' + full_path_image
            os.remove(path1)
            os.remove(path2)
        raise error 