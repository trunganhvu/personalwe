from mainapp.model.Category import Category
from mainapp.Common import DateTime
from datetime import datetime

def get_all_category():
    """
    Get all category
    """
    category_list = Category.objects.all().order_by('-category_id')
    return category_list

def insert_category(category):
    """
    Insert category
    """
    category = Category(category_name=category.category_name,
                category_url=category.category_url,
                display=category.display,
                display_order=category.display_order,
                category_image_default_name=category.category_image_default_name,
                category_image_default=category.category_image_default,
                display_type=category.display_type,
                created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                )
    category.save()
    return category

def get_category_detail(id):
    """
    Get category detail
    """
    category = Category.objects.get(pk=id)
    return category

def update_category(category):
    """
    Update category
    """
    print('dao')
    category_db = Category.objects.get(pk=category.category_id)
    category_db.category_name = category.category_name 
    category_db.category_url = category.category_url
    category_db.display_order = category.display_order
    category_db.display = category.display
    category_db.category_image_default_name = category.category_image_default_name
    category_db.category_image_default = category.category_image_default
    category_db.display_type = category.display_type
    category_db.save()
    return category_db

def get_category_display():
    """
    Get all category display
    """
    category_list = Category.objects.filter(display=True).order_by('display_order')
    return category_list

def get_category_detail_diplay(url):
    """
    Get category detail is diplay
    """
    category = Category.objects.filter(category_url=url).first()
    return category

def delete_category_by_id(id):
    """
    Delete category by id
    """
    category = Category.objects.get(pk=id)
    category.delete()