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
    print('dao 1')

    category = Category(category_name=category_name,
                category_url=category_url,
                display=category_display,
                display_order=category_display_order,
                category_image_default_name=category_image_name,
                category_image_default=category_image,
                created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                )
    print('dao 2')
    category.save()
    print('dao 3')
