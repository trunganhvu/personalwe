from mainapp.model.Product import Product
from datetime import datetime

def get_all_product():
    """
    Get all product
    """
    list_product = Product.objects.all().order_by('-product_id')
    return list_product

def get_product_detail_by_id(product_id):
    """
    Get product detail by id
    """
    product = Product.objects.get(pk=product_id)
    return product