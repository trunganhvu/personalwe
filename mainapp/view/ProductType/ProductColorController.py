from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from mainapp.service.ProductType import ProductColorService
from mainapp.model.ProductColor import ProductColor
from mainapp.Common import ConstValiable

@login_required(login_url='/login/')
def view_product_color_detail_by_id(request, product_type_id, product_color_id):
    """
    View color detail by id - need auth
    """
    product_color = ProductColorService.get_product_color_detail_by_id(product_color_id)
    context = {
        'product_color': product_color,
        'product_type_id': product_type_id
    }
    return render(request, 'private/ProductType/productcolordetail.html', context)

@login_required(login_url='/login/')
def view_product_color_insert_form_page(request, product_type_id):
    """
    View page insert product color - need auth
    """
    context = {
        'product_type_id': product_type_id
    }
    return render(request, 'private/ProductType/productcolorform.html', context=context)

@login_required(login_url='/login/')
def view_product_color_update_form_page(request, product_type_id, product_color_id):
    """
    View page update product color - need auth
    """
    try:
        product_color = ProductColorService.get_product_color_detail_by_id(product_color_id)
        context = {
            'product_color': product_color,
            'product_type_id': product_type_id
        }
        return render(request, 'private/ProductType/productcolorform.html', context=context)
    except Exception:
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/product-type/' + str(product_type_id))

@login_required(login_url='/login/')
def insert_product_color(request, product_type_id):
    """
    Insert product type - need auth
    """
    try:
        if request.method == 'POST':
            type_id = request.POST.get('type-id')
            color_code = request.POST.get('color-code')
            color_name = request.POST.get('color-name')
            
            product_color = ProductColor(product_type_id_id=type_id, 
                                    product_color_code=color_code,
                                    product_color_name=color_name,
                                    )
            
            context = {
                'product_color': product_color
            }
            check = validate_product_color(product_color)
            if check:
                ProductColorService.insert_product_color(product_color)
                messages.success(request, ConstValiable.MESSAGE_POPUP_SUCCESS)
                return redirect('/product-type/' + str(product_type_id))
            else:
                messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
                return render(request, 'private/ProductType/productcolorform.html', context=context)
    except Exception:
        print('error')
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/product-type/' + str(product_type_id))

@login_required(login_url='/login/')
def update_product_color(request, product_type_id, product_color_id):
    """
    Update product type - need auth
    """
    try:
        if request.method == 'POST':
            type_id = request.POST.get('type-id')
            color_code = request.POST.get('color-code')
            color_name = request.POST.get('color-name')

            product_color = ProductColor(product_color_id=product_color_id,
                                    product_type_id_id=type_id, 
                                    product_color_code=color_code,
                                    product_color_name=color_name,
                                    )
            context = {
                'product_color': product_color
            }
            check = validate_product_color(product_color)
            if check:
                ProductColorService.update_product_color(product_color)
                messages.success(request, ConstValiable.MESSAGE_POPUP_SUCCESS)
                return redirect('/product-type/' + str(product_type_id) + '/product-color/' + str(product_color_id))
            else:
                messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
                return render(request, 'private/ProductType/productcolorform.html', context=context)
    except Exception:
        print('error')
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/product-type/' + str(product_type_id))

@login_required(login_url='/login/')
def delete_product_color_by_id(request, product_type_id, product_color_id):
    """
    Delete product color
    """
    try:
        ProductColorService.delete_product_color_by_id(product_color_id)
        messages.success(request, ConstValiable.MESSAGE_POPUP_SUCCESS)
    
    except Exception:
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
    return redirect('/product-type/' + str(product_type_id))

def validate_product_color(product_color):
    """
    Validation product color
    """
    if product_color.product_color_code is None or len(product_color.product_color_code) > 25:
        return False
    if product_color.product_color_name is None or len(product_color.product_color_name) > 255:
        return False
    return True