from mainapp.model.Product import Product
from datetime import datetime

def get_all_product_in_type(product_id):
    """
    Get all product
    """
    list_product = Product.objects.filter(pk=product_id).order_by('-product_id')
    return list_product

def get_product_detail_by_id(product_id):
    """
    Get product detail by id
    """
    product = Product.objects.get(pk=product_id)
    return product

def insert_product(product):
    """
    Insert product
    """
    p = Product(product_code=product.product_code,
                product_name=product.product_name,
                product_description=product.product_description,
                product_detail=product.product_detail,
                product_type_id=product.product_type_id,
                created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    p.save()
    return p

def update_product(product):
    """
    Update product
    """
    p = Product.objects.get(pk=product.product_id)
    p.product_code = product.product_code 
    p.product_name = product.product_name
    p.product_description = product.product_description
    p.product_detail = product.product_detail
    p.product_type_id = product.product_type_id
    p.save()
    return p
    
def delete_product(product_id):
    """
    Delete product
    """
    product = Product.objects.get(pk=product_id)
    product.delete()
