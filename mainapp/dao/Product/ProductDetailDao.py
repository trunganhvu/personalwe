from mainapp.model.ProductDetail import ProductDetail
from datetime import datetime

def get_all_detail_product_by_product_id(product_id):
    """
    Get detail by product id
    """
    list_detail = ProductDetail.objects.filter(product_id=product_id)
    return list_detail

def insert_product_detail(product_detail):
    """
    Insert product detail
    """
    p_detail = ProductDetail(product_id=product_detail.product_id,
                            product_original_price=product_detail.product_original_price,
                            product_public_price=product_detail.product_public_price,
                            product_color_id=product_detail.product_color_id,
                            product_size_id=product_detail.product_size_id,
                            created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    p_detail.save()
    return p_detail

def update_product_detail(product_detail):
    """
    Update product detail
    """
    p_detail = ProductDetail.objects.get(pk=product_detail.product_detail_id)
    p_detail.product_original_price = product_detail.product_original_price
    p_detail.product_public_price = product_detail.product_public_price
    p_detail.product_color_id = product_detail.product_color_id
    p_detail.product_size_id = product_detail.product_size_id
    p_detail.save()
    return p_detail

def delete_product_detail_by_pk(product_detail_id):
    """
    Delete product detail by id
    """
    p_detail = ProductDetail.objects.get(pk=product_detail_id)
    p_detail.delete()

def delete_product_detail_by_product_id(product_id):
    """
    Delete product detail by id
    """
    p_detail = ProductDetail.objects.filter(product_id=product_id)
    p_detail.delete()