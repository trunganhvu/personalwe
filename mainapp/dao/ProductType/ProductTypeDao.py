from mainapp.model.ProductType import ProductType
from datetime import datetime

def get_all_product_type():
    """
    Get all product type
    """
    product_types = ProductType.objects.all().order_by('-product_type_id')
    return product_types

def get_product_type_detail_by_id(id):
    """
    View type detail by id
    """
    product_type = ProductType.objects.get(pk=id)
    return product_type

def insert_product_type(product_type):
    """
    Insert product type
    """
    p_type = ProductType(product_type_code=product_type.product_type_code,
                        product_type_name=product_type.product_type_name,
                        product_type_description=product_type.product_type_description,
                        created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    p_type.save()
    return p_type

def update_product_type(product_type):
    """
    Update product type
    """
    p_type = ProductType.objects.get(pk=product_type.product_type_id)
    p_type.product_type_code = product_type.product_type_code
    p_type.product_type_name = product_type.product_type_name
    p_type.product_type_description = product_type.product_type_description
    p_type.save()
    return p_type

def delete_product_type_by_id(product_type_id):
    """
    Delete product type by id
    """
    p_type = ProductType.objects.get(pk=product_type_id)
    p_type.delete()