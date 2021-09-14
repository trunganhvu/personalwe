from django.conf import settings
from datetime import datetime
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from mainapp.Common import Util
from mainapp.service.Product import ProductService, ProductDetailService, ProductImageService
from mainapp.service.ProductType import ProductTypeService, ProductColorService, ProductSizeService
from mainapp.Common import ConstValiable

@login_required(login_url='/login/')
def view_all_product_page(request):
    """
    View all product
    """
    product_types = ProductTypeService.get_all_product_type()
    list_product_type = []
    for product_type in product_types:
        list_product = ProductService.get_all_product_in_type(product_type.product_type_id)
        p_type = {
            'list_product': list_product,
            'product_type': product_type
        }
        list_product_type.append(p_type)
    context = {
        'list_product_type': list_product_type
    }
    return render(request, 'private/Product/product.html', context)

@login_required(login_url='/login/')
def view_product_detail_page(request, product_id):
    """
    View product detail page
    """
    try:
        # Get base info product       
        product = ProductService.get_product_detail_by_id(product_id)
        if product is not None:
            # Get list detail info product
            list_p_detail = ProductDetailService.get_all_detail_product_by_product_id(product.product_id)
            
            # Get list image of product
            list_p_image = ProductImageService.get_all_product_image_by_product_id(product.product_id)

            # Get list promotion of product

            context = {
                'product': product,
                'list_product_detail': list_p_detail,
                'list_product_image': list_p_image
            }
            return render(request, 'private/Product/productdetail.html', context=context)
        else:
            raise Exception('Product not exist')
    except Exception as error:
        print(error)
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/products/')