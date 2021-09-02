from mainapp.model.Category import Category
from mainapp.Common import DateTime
from datetime import datetime

def get_all_category():
    """
    Get all category
    """
    category_list = Category.objects.all()
    return category_list

# def insert_header_image(header_name, header_path):
#     """
#     Insert header
#     """
#     create_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     header = Header(image_default_name=header_name, image_default_path=header_path, created_at=create_at, active=True)
#     header.save()

# def count_header_image():
#     """
#     Count header image
#     """
#     count_header_image = Header.objects.filter(active=True).count()
#     return count_header_image