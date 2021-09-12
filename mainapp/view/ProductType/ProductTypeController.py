from mainapp.model.ProductType import ProductType
from django.conf import settings
from django.conf.urls import url
from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from mainapp.service.ProductType import ProductTypeService, ProductSizeService, ProductColorService
from mainapp.Common import ConstValiable

@login_required(login_url='/login/')
def get_all_product_type(request):
    """
    Get all product type - need auth
    """
    product_type_list = ProductTypeService.get_all_product_type()
    context = {
        'product_type_list': product_type_list
    }
    return render(request, 'private/ProductType/producttype.html', context)

@login_required(login_url='/login/')
def view_product_type_detail_by_id(request, product_type_id):
    """
    View type detail by id
    """
    try:
        product_type = ProductTypeService.get_product_type_detail_by_id(product_type_id)
        list_product_size = ProductSizeService.get_all_product_size_in_product_type(product_type_id)
        list_product_color = ProductColorService.get_all_product_color_in_type(product_type_id)
        
        context = {
            'product_type': product_type,
            'list_product_size': list_product_size,
            'list_product_color': list_product_color
        }
        return render(request, 'private/ProductType/producttypedetail.html', context)
    except Exception:
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/product-type')


@login_required(login_url='/login/')
def view_product_type_insert_form_page(request):
    """
    View page insert product type
    """
    return render(request, 'private/ProductType/producttypeform.html')


@login_required(login_url='/login/')
def view_product_type_update_form_page(request, product_type_id):
    """
    View page update product type
    """
    context = {}
    try:
        product_type = ProductTypeService.get_product_type_detail_by_id(product_type_id)
        context = {
            'product_type': product_type
        }
    except Exception:
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/product-type')

    return render(request, 'private/ProductType/producttypeform.html', context=context)

@login_required(login_url='/login/')
def insert_product_type(request):
    """
    Insert product type
    """
    try:
        if request.method == 'POST':
            type_code = request.POST.get('type-code')
            type_name = request.POST.get('type-name')
            type_description = request.POST.get('type-description')
            product_type = ProductType(product_type_code=type_code,
                                    product_type_name=type_name,
                                    product_type_description=type_description)
            context = {
                'product_type': product_type
            }
            check = validate_product_type(product_type)
            if check:
                ProductTypeService.insert_product_type(product_type)
                messages.success(request, ConstValiable.MESSAGE_POPUP_SUCCESS)
                return redirect('/product-type')
            else:
                messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
                return render(request, 'private/ProductType/producttypeform.html', context=context)

    except Exception:
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/product-type')

@login_required(login_url='/login/')
def update_product_type(request, product_type_id):
    """
    Update product type
    """
    try:
        if request.method == 'POST':
            type_id = request.POST.get('type-id')
            type_code = request.POST.get('type-code')
            type_name = request.POST.get('type-name')
            type_description = request.POST.get('type-description')
            product_type = ProductType(product_type_id=type_id,
                                    product_type_code=type_code,
                                    product_type_name=type_name,
                                    product_type_description=type_description)
            context = {
                'product_type': product_type
            }
            check = validate_product_type(product_type)
            print(check)
            if check:
                ProductTypeService.update_product_type(product_type)
                messages.success(request, ConstValiable.MESSAGE_POPUP_SUCCESS)
                return redirect('/product-type/' + str(product_type_id))
            else:
                messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
                return render(request, 'private/ProductType/producttypeform.html', context=context)
            
    except Exception:
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/product-type/' + str(product_type_id))

@login_required(login_url='/login/')
def delete_product_type_by_id(request, product_type_id):
    """
    Delete product type by id
    """
    try:
        ProductTypeService.delete_product_type_by_id(product_type_id)
        messages.success(request, ConstValiable.MESSAGE_POPUP_SUCCESS)
    
    except Exception:
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
    return redirect('/product-type')


def validate_product_type(product_type):
    """
    Validation product type
    """
    if product_type.product_type_code is None or len(product_type.product_type_code) > 25:
        return False
    if product_type.product_type_name is None or len(product_type.product_type_name) > 255:
        return False
    if product_type.product_type_description is None or len(product_type.product_type_description) > 1000:
        return False
    return True