from django.conf import settings
from datetime import datetime
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from mainapp.Common import Util
from mainapp.service.Product import ProductService
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
        product = ProductService.get_event_detail_by_id(product_id)
        # list_p_detail = Pro
        context = {
            'product': product,
        }
        return render(request, 'private/Product/productdetail.html', context=context)
    except Exception:
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/product-type')