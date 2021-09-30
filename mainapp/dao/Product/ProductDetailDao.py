from mainapp.model.ProductDetail import ProductDetail
from datetime import datetime
from django.utils import timezone

def get_all_detail_product_by_product_id(product_id):
    """
    Get detail by product id
    """
    # list_detail = ProductDetail.objects.filter(product_id=product_id).select_related('product_color_id__product_color_id',
    #                                                                                 'product_color_id__product_color_code',
    #                                                                                 'product_color_id__product_color_name',
    #                                                                                 'product_size_id__product_size_id',
    #                                                                                 'product_size_id__product_size_code',
    #                                                                                 'product_size_id__product_size_name',
    #                                                                                 'product_size_id__product_size_height_max',
    #                                                                                 'product_size_id__product_size_height_min',
    #                                                                                 'product_size_id__product_size_width_max',
    #                                                                                 'product_size_id__product_size_width_min')
    list_detail = ProductDetail.objects.filter(product_id=product_id).select_related('product_color_id',
                                                                                    'product_size_id',
                                                                                    )
    return list_detail

def get_product_detail_by_product_detail_id(product_detail_id):
    """
    Get product detail by product detail id
    """
    product_detail = ProductDetail.objects.get(pk=product_detail_id)
    return product_detail

def get_product_detail_by_product_id_size_id_color_id(product_id, product_size_id, product_color_id):
    """
    View detail by product id, size, color
    """
    product_detail = ProductDetail.objects.filter(product_id=product_id,
                                                product_color_id=product_color_id,
                                                product_size_id=product_size_id).first()
    return product_detail

def insert_product_detail(product_detail):
    """
    Insert product detail
    """
    p_detail = ProductDetail(product_id=product_detail.product_id,
                            product_original_price=product_detail.product_original_price,
                            product_public_price=product_detail.product_public_price,
                            product_color_id=product_detail.product_color_id,
                            product_size_id=product_detail.product_size_id,
                            number_of_product=product_detail.number_of_product,
                            product_in_stock=product_detail.product_in_stock,
                            created_at=datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S"))
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
    p_detail.number_of_product = product_detail.number_of_product
    p_detail.product_in_stock = product_detail.product_in_stock
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