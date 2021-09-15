from mainapp.model.Product import Product
from mainapp.model.ProductDetail import ProductDetail
from datetime import datetime
from django.utils import timezone
from django.db import transaction

def get_all_product_in_type(product_type_id):
    """
    Get all product
    """
    list_product = Product.objects.filter(product_type_id=product_type_id).order_by('-product_id')
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
                created_at=datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S"))
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

def insert_product_and_detail(product, list_product_detail):
    """
    Insert product and detail product
    """
    print('dao 1')
    with transaction.atomic():
        print('dao 11')
        p = Product(product_code=product.product_code,
                    product_name=product.product_name,
                    product_description=product.product_description,
                    product_detail=product.product_detail,
                    product_type_id=product.product_type_id,
                    created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        p.save()
        print('dao 2')
        for product_detail in list_product_detail:
            print('dao for 1')
            product_detail.product_id = p
            print('dao for 2')
            p_detail = ProductDetail(product_id=product_detail.product_id,
                            product_original_price=product_detail.product_original_price,
                            product_public_price=product_detail.product_public_price,
                            product_color_id=product_detail.product_color_id,
                            product_size_id=product_detail.product_size_id,
                            created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            print('dao for 4')
            p_detail.save()