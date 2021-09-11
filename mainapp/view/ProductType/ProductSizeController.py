from django.conf import settings
from django.conf.urls import url
from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from mainapp.service.ProductType import ProductSizeService
from mainapp.model.ProductSize import ProductSize
from mainapp.Common import ConstValiable

@login_required(login_url='/login/')
def view_product_size_detail_by_id(request, product_size_id):
    """
    View size detail by id - need auth
    """
    product_size = ProductSizeService.get_product_size_detail_by_id(product_size_id)
    
    context = {
        'product_size': product_size,
    }
    return render(request, 'private/ProductType/producttypedetail.html', context)

@login_required(login_url='/login/')
def view_product_size_insert_form_page(request, product_type_id):
    """
    View page insert product size - need auth
    """
    context = {
        'product_type_id': product_type_id
    }
    return render(request, 'private/ProductType/productsizeform.html', context=context)

@login_required(login_url='/login/')
def view_product_size_update_form_page(request, product_type_id, product_size_id):
    """
    View page update product size - need auth
    """
    try:
        product_size = ProductSizeService.get_product_size_detail_by_id(product_size_id)
        context = {
            'product_size': product_size,
            'product_type_id': product_type_id
        }
        return render(request, 'private/ProductType/productsizeform.html', context=context)
    except Exception:
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/product-type/' + str(product_type_id))

@login_required(login_url='/login/')
def view_product_size_detail_by_id(request, product_type_id, product_size_id):
    """
    View size detail by id - need auth
    """
    try:
        product_size = ProductSizeService.get_product_size_detail_by_id(product_size_id)

        context = {
            'product_size': product_size,
            'product_type_id': product_type_id
        }
        print(context)
        return render(request, 'private/ProductType/productsizedetail.html', context)
    except Exception:
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/product-type/' + str(product_type_id))

@login_required(login_url='/login/')
def insert_product_size(request, product_type_id):
    """
    Insert product type - need auth
    """
    try:
        if request.method == 'POST':
            type_id = request.POST.get('type-id')
            size_code = request.POST.get('size-code')
            size_name = request.POST.get('size-name')
            size_height_min = 0
            size_height_max = 0
            size_width_min = 0
            size_width_max = 0
            if request.POST.get('size-height-min') is not None and request.POST.get('size-height-min') != '':
                size_height_min = request.POST.get('size-height-min') 
            if request.POST.get('size-height-max') is not None and request.POST.get('size-height-max') != '':
                size_height_max = request.POST.get('size-height-max')
            if request.POST.get('size-width-min') is not None and request.POST.get('size-width-min') != '':
                size_width_min = request.POST.get('size-width-min')
            if request.POST.get('size-width-max') is not None and request.POST.get('size-width-max') != '':
                size_width_max = request.POST.get('size-width-max')

            product_size = ProductSize(product_type_id_id=type_id, 
                                    product_size_code=size_code,
                                    product_size_name=size_name,
                                    product_size_height_max=size_height_max,
                                    product_size_height_min=size_height_min,
                                    product_size_width_max=size_width_max,
                                    product_size_width_min=size_width_min)
            
            context = {
                'product_size': product_size
            }
            check = validate_product_size(product_size)
            if check:
                ProductSizeService.insert_product_size(product_size)
                messages.success(request, ConstValiable.MESSAGE_POPUP_SUCCESS)
                return redirect('/product-type/' + str(product_type_id))
            else:
                messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
                return render(request, 'private/ProductType/productsizeform.html', context=context)
    except Exception:
        print('error')
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/product-type/' + str(product_type_id))

@login_required(login_url='/login/')
def update_product_size(request, product_type_id, product_size_id):
    """
    Update product type - need auth
    """
    try:
        if request.method == 'POST':
            type_id = request.POST.get('type-id')
            size_code = request.POST.get('size-code')
            size_name = request.POST.get('size-name')
            size_height_min = 0
            size_height_max = 0
            size_width_min = 0
            size_width_max = 0
            if request.POST.get('size-height-min') is not None and request.POST.get('size-height-min') != '':
                size_height_min = request.POST.get('size-height-min') 
            if request.POST.get('size-height-max') is not None and request.POST.get('size-height-max') != '':
                size_height_max = request.POST.get('size-height-max')
            if request.POST.get('size-width-min') is not None and request.POST.get('size-width-min') != '':
                size_width_min = request.POST.get('size-width-min')
            if request.POST.get('size-width-max') is not None and request.POST.get('size-width-max') != '':
                size_width_max = request.POST.get('size-width-max')

            product_size = ProductSize(product_size_id=product_size_id,
                                    product_type_id_id=type_id, 
                                    product_size_code=size_code,
                                    product_size_name=size_name,
                                    product_size_height_max=size_height_max,
                                    product_size_height_min=size_height_min,
                                    product_size_width_max=size_width_max,
                                    product_size_width_min=size_width_min)
            
            context = {
                'product_size': product_size
            }
            check = validate_product_size(product_size)
            if check:
                ProductSizeService.update_product_size(product_size)
                messages.success(request, ConstValiable.MESSAGE_POPUP_SUCCESS)
                return redirect('/product-type/' + str(product_type_id) + '/product-size/' + str(product_size_id))
            else:
                messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
                return render(request, 'private/ProductType/productsizeform.html', context=context)
    except Exception:
        print('error')
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/product-type/' + str(product_type_id))

@login_required(login_url='/login/')
def delete_product_size_by_id(request, product_type_id, product_size_id):
    """
    Delete product size
    """
    try:
        ProductSizeService.delete_product_size_by_id(product_size_id)
        messages.success(request, ConstValiable.MESSAGE_POPUP_SUCCESS)
    
    except Exception:
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
    return redirect('/product-type/' + str(product_type_id))

def validate_product_size(product_size):
    """
    Validation product size
    """
    if product_size.product_size_code is None or len(product_size.product_size_code) > 25:
        return False
    if product_size.product_size_name is None or len(product_size.product_size_name) > 255:
        return False
    return True