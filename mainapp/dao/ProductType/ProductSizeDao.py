from mainapp.model.ProductSize import ProductSize
from datetime import datetime

def get_all_product_size_in_product_type(product_type_id):
    """
    Get all size in type
    """
    list_size = ProductSize.objects.filter(product_type_id=product_type_id)
    return list_size

def get_product_size_detail_by_id(product_size_id):
    """
    Get product size detail by id
    """
    product_size = ProductSize.objects.filter(product_size_id=product_size_id).first()
    return product_size

def insert_product_size(product_size):
    """
    Insert product size
    """
    p_size = ProductSize(product_size_code=product_size.product_size_code,
                        product_size_name=product_size.product_size_name,
                        product_type_id=product_size.product_type_id,
                        product_size_height_max=product_size.product_size_height_max,
                        product_size_height_min=product_size.product_size_height_min,
                        product_size_width_max=product_size.product_size_width_max,
                        product_size_width_min=product_size.product_size_width_min,
                        created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    p_size.save()
    return p_size

def update_product_size(product_size):
    """
    Update product size
    """
    p_size = ProductSize.objects.get(pk=product_size.product_size_id)
    p_size.product_size_code = product_size.product_size_code
    p_size.product_size_name = product_size.product_size_name
    p_size.product_type_id = product_size.product_type_id
    p_size.product_size_height_max = product_size.product_size_height_max
    p_size.product_size_height_min = product_size.product_size_height_min
    p_size.product_size_width_max = product_size.product_size_width_max
    p_size.product_size_width_min = product_size.product_size_width_min
    p_size.save()
    return p_size

def delete_product_size_by_id(product_size_id):
    """
    Delete product size
    """
    p_size = ProductSize.objects.get(pk=product_size_id)
    p_size.delete()