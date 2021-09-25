from datetime import datetime
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib import messages
import math

from mainapp.model.ProductPromotion import ProductPromotion
from mainapp.service.Product import ProductService, ProductPromotionService, ProductImageService, ProductDetailService
from mainapp.service.ProductType import ProductTypeService
from mainapp.Common import ConstValiable
from mainapp.service.Event import EventService

def get_all_product(request):
    """
    Get all product
    """
    list_product = ProductService.get_all_product()
    list_product_type = ProductTypeService.get_all_product_type()
    list_p = []
    for product in list_product:
        product_image = ProductImageService.get_one_product_image_by_product_id(product.product_id)
        item = {
            'product': product,
            'product_image': product_image
        }
        list_p.append(item)
    context = {
        'list_product': list_p,
        'list_product_type': list_product_type,
    }
    return render(request, 'public/Product/listproduct.html', context=context)


def get_all_product_in_product_type_id(request, product_type_id):
    """
    Get all product in product type id
    """
    list_product = ProductService.get_all_product_in_type(product_type_id)
    list_product_type = ProductTypeService.get_all_product_type()
    list_p = []
    if list_product is not None:
        for product in list_product:
            product_image = ProductImageService.get_one_product_image_by_product_id(product.product_id)
            item = {
                'product': product,
                'product_image': product_image
            }
            list_p.append(item)
    context = {
        'list_product': list_p,
        'list_product_type': list_product_type,
    }
    return render(request, 'public/Product/listproduct.html', context=context)

def get_product_detail_by_product_id(request, product_id):
    """
    Get product detail by product id
    """
    # Get product
    product = ProductService.get_product_detail_by_id(product_id)
    if product is not None:
        list_product_image = []
        list_product_detail = []
        # Get all type
        list_product_type = ProductTypeService.get_all_product_type()

        # Get list image of product
        list_product_image = ProductImageService.get_all_product_image_by_product_id(product.product_id)

        # Get detail
        list_product_detail = ProductDetailService.get_all_detail_product_by_product_id(product.product_id)

        list_product_color = []
        list_product_size = []
        min_public_price = 0
        list_public_price = []
        total_product_in_stock = 0
        if list_product_detail is not None and list_product_detail.count() > 0:
            for p_detail in list_product_detail:
                # List color
                product_color = {
                    'product_color_code': p_detail.product_color_id.product_color_code,
                    'product_color_id': p_detail.product_color_id.product_color_id,
                    'product_color_name': p_detail.product_color_id.product_color_name,
                }
                if not product_color in list_product_color:
                    list_product_color.append(product_color)

                # List size
                product_size = {
                    'product_size_id': p_detail.product_size_id.product_size_id,
                    'product_size_code': p_detail.product_size_id.product_size_code,
                    'product_size_name': p_detail.product_size_id.product_size_name,
                    'product_size_height_max': p_detail.product_size_id.product_size_height_max,
                    'product_size_height_min': p_detail.product_size_id.product_size_height_min,
                    'product_size_width_max': p_detail.product_size_id.product_size_width_max,
                    'product_size_width_min': p_detail.product_size_id.product_size_width_min,
                }
                if not product_size in list_product_size:
                    list_product_size.append(product_size)
                
                # List price
                list_public_price.append(p_detail.product_public_price)

                # Total product
                total_product_in_stock += p_detail.product_in_stock

            # Price min in list price
            min_public_price = min(list_public_price)

            # Remove .00 in price
            min_public_price = math.floor(min_public_price)

        context = {
            'product': product,
            'list_product_type': list_product_type,
            'list_product_image': list_product_image,
            'list_product_detail': list_product_detail,
            'list_product_color': list_product_color,
            'list_product_size': list_product_size,
            'min_public_price': f'{min_public_price:,}',
            'total_product_in_stock': total_product_in_stock,
            'length_total_product_in_stock': len(str(total_product_in_stock)),
        }
        return render(request, 'public/Product/productdetail.html', context=context)
    else:
        return redirect('/shop/')