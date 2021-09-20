from datetime import datetime
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib import messages

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
        list_product_image = ProductImageService.get_one_product_image_by_product_id(product.product_id)

        # Get detail
        list_product_detail = ProductDetailService.get_all_detail_product_by_product_id(product.product_id)

        context = {
            'product': product,
            'list_product_type': list_product_type,
            'list_product_image': list_product_image,
            'list_product_detail': list_product_detail,
        }
        return render(request, 'public/Product/productdetail.html', context=context)
    else:
        return redirect('/shop/')