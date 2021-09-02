from mainapp.model.Category import Category
from mainapp.Common import DateTime
from datetime import datetime

def get_all_category():
    """
    Get all category
    """
    category_list = Category.objects.all()
    return category_list

def insert_category(category_name, category_url, category_image_name, category_image, category_display, category_display_order):
    """
    Insert category
    """
    category = Category(category_name=category_name,
                category_url=category_url,
                display=category_display,
                display_order=category_display_order,
                category_image_default_name=category_image_name,
                category_image_default=category_image,
                created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                )
    category.save()

def get_category_detail(id):
    """
    Get category detail
    """
    category = Category.objects.get(pk=id)
    return category