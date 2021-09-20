from datetime import datetime
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from mainapp.model.ProductPromotion import ProductPromotion
from mainapp.service.Product import ProductService, ProductPromotionService
from mainapp.Common import ConstValiable
from mainapp.service.Event import EventService

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
            # Get list event
            list_event = EventService.get_all_event_active()

            context = {
                'product': product,
                'list_event': list_event
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

            # Get list event
            list_event = EventService.get_all_event_active()

            context = {
                'product': product,
                'product_promotion': product_promotion,
                'list_event': list_event
            }
            return render(request, 'private/Product/productpromotionform.html', context=context)
        else:
            raise Exception('Product not exist')
    except Exception as error:
        print(error)
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/products/' + str(product_id))

def insert_product_promotion(request, product_id):
    """
    Insert product promotion
    """
    try:
        if request.method == 'POST':
            # Get base info product       
            product = ProductService.get_product_detail_by_id(product_id)
            if product is not None:
                

                # Get data in request
                product_promotion_start = request.POST.get('product-promotion-start')
                product_promotion_end = request.POST.get('product-promotion-end')
                event = request.POST.get('event')
                discount = request.POST.get('discount')

                # Convert type str to date
                product_promotion_start = datetime.strptime(product_promotion_start, ConstValiable.FORMAT_DATE1)
                product_promotion_end = datetime.strptime(product_promotion_end, ConstValiable.FORMAT_DATE1)

                print(product_promotion_start)
                product_promotion = ProductPromotion(product_promotion_start=product_promotion_start,
                                                    product_promotion_end=product_promotion_end,
                                                    event_id_id=event,
                                                    discount=discount,
                                                    product_id_id=product_id)

                check = validate_list_data(product_promotion)
                print('controller check=' + str(check))
                if check:
                    print('befor insert')
                    # Insert
                    ProductPromotionService.insert_product_promotion(product_promotion)
                    messages.success(request, ConstValiable.MESSAGE_POPUP_SUCCESS)

                    return redirect('/products/' + str(product_id))
                else:
                    # Get list event
                    list_event = EventService.get_all_event_active()
                    context = {
                        'product': product,
                        'list_event': list_event,
                        'product_promotion': product_promotion
                    }
                    messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
                    return render(request, 'private/Product/productpromotionform.html', context=context)
            else:
                raise Exception('Product not exist')
        else:
            raise Exception('Don\'t use method GET')
    except Exception as error:
        print(error)
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/products/' + str(product_id))

def update_product_promotion(request, product_id, product_promotion_id):
    """
    Update product promotion
    """
    try:
        if request.method == 'POST':
            # Get base info product       
            product = ProductService.get_product_detail_by_id(product_id)

            # Get product promotion
            p_promotion = ProductPromotionService.get_product_promotion_detail_by_promotion_id(product_promotion_id)
            
            if product is not None and p_promotion is not None:
                # Get data in request
                p_promotion_id = request.POST.get('product-promotion-id')
                product_promotion_start = request.POST.get('product-promotion-start')
                product_promotion_end = request.POST.get('product-promotion-end')
                event = request.POST.get('event')
                discount = request.POST.get('discount')

                # Convert type str to date
                product_promotion_start = datetime.strptime(product_promotion_start, ConstValiable.FORMAT_DATE1)
                product_promotion_end = datetime.strptime(product_promotion_end, ConstValiable.FORMAT_DATE1)

                product_promotion = ProductPromotion(product_promotion_id=p_promotion_id,
                                                    product_promotion_start=product_promotion_start,
                                                    product_promotion_end=product_promotion_end,
                                                    event_id_id=event,
                                                    discount=discount,
                                                    product_id_id=product_id)

                check = validate_list_data(product_promotion)
                print(check)
                if check:
                    # Update
                    ProductPromotionService.update_product_promotion(product_promotion)
                    messages.success(request, ConstValiable.MESSAGE_POPUP_SUCCESS)

                    return redirect('/products/' + str(product_id) + '/promotion/' + str(p_promotion_id) + '/')
                else:
                    # Get list event
                    list_event = EventService.get_all_event_active()
                    context = {
                        'product': product,
                        'list_event': list_event,
                        'product_promotion': product_promotion
                    }
                    messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
                    return render(request, 'private/Product/productpromotionform.html', context=context)
            else:
                raise Exception('Product not exist')
        else:
            raise Exception('Don\'t use method GET')
    except Exception as error:
        print(error)
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/products/' + str(product_id))

def delete_product_promotion_by_promotion_id(request, product_id, product_promotion_id):
    """
    Delete product promotion
    """
    try:
        ProductPromotionService.delete_product_promotion(product_promotion_id)
        messages.success(request, ConstValiable.MESSAGE_POPUP_SUCCESS)
    
    except Exception:
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
    return redirect('/products/' + str(product_id))

def validate_list_data(product_promotion):
    """
    Validate data
    """
    if int(product_promotion.discount) < 0 or int(product_promotion.discount) > 100:
        return False
    if product_promotion.product_promotion_start > product_promotion.product_promotion_end:
        return False
    return True