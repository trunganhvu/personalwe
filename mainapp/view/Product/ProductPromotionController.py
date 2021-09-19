from datetime import datetime
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from mainapp.Common import Util
from mainapp.service.Product import ProductService, ProductPromotionService
from mainapp.Common import ConstValiable

@login_required(login_url='/login/')
def view_detail_product_promotion_by_promotion_id(request, product_id, product_promotion_id):
    """
    View page detail promotion by id - need auth
    """
    try:
        # Get base info product       
        product = ProductService.get_product_detail_by_id(product_id)
        if product is not None:
            # Get detail promotion
            product_promotion = ProductPromotionService.get_product_promotion_detail_by_promotion_id(product_promotion_id)

            context = {
                'product': product,
                'product_promotion': product_promotion
            }
            return render(request, 'private/Product/productpromotiondetail.html', context=context)
        else:
            raise Exception('Product not exist')
    except Exception as error:
        print(error)
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/products/' + str(product_id))

@login_required(login_url='/login/')
def view_product_promotion_form_insert_page(request, product_id):
    """
    View form insert product promotion
    """
    try:
        # Get base info product       
        product = ProductService.get_product_detail_by_id(product_id)
        if product is not None:

            context = {
                'product': product,
            }
            return render(request, 'private/Product/productpromotionform.html', context=context)
        else:
            raise Exception('Product not exist')
    except Exception as error:
        print(error)
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/products/' + str(product_id))

@login_required(login_url='/login/')
def view_product_promotion_form_update_page(request, product_id, product_promotion_id):
    """
    View form update product promotion
    """
    try:
        # Get base info product       
        product = ProductService.get_product_detail_by_id(product_id)
        if product is not None:
            # Get detail promotion
            product_promotion = ProductPromotionService.get_product_promotion_detail_by_promotion_id(product_promotion_id)

            context = {
                'product': product,
                'product_promotion': product_promotion
            }
            return render(request, 'private/Product/productpromotionform.html', context=context)
        else:
            raise Exception('Product not exist')
    except Exception as error:
        print(error)
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/products/' + str(product_id))