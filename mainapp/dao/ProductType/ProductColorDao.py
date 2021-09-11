from mainapp.model.ProductColor import ProductColor
from datetime import datetime

def get_all_product_color_in_type(product_type_id):
    """
    Get all color in type
    """
    list_product_color = ProductColor.objects.first(product_type_id=product_type_id)
    return list_product_color

def get_product_color_detail_by_id(product_color_id):
    """
    Get color detail by id
    """
    product_color = ProductColor.objects.get(pk=product_color_id)
    return product_color

def insert_product_color(product_color):
    """
    Insert product color
    """
    p_color = ProductColor(product_color_code=product_color.product_color_code,
                            product_color_name=product_color.product_color_code,
                            product_type_id=product_color.product_type_id,
                            created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    p_color.save()
    return p_color

def update_product_color(product_color):
    """
    Update product color
    """
    p_color = ProductColor.objects.get(pk=product_color.product_color_id)
    p_color.product_color_code=product_color.product_color_code
    p_color.product_color_name=product_color.product_color_code,
    p_color.product_type_id=product_color.product_type_id,
    p_color.save()
    return p_color

def delete_product_color_by_id(product_color_id):
    """
    Delete color by id
    """
    p_color = ProductColor.objects.get(pk=product_color_id)
    p_color.delete()