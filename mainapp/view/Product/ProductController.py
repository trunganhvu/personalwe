from django.conf import settings
from datetime import datetime
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from decimal import *

from mainapp.Common import Util
from mainapp.service.Product import ProductService, ProductDetailService, ProductImageService, ProductPromotionService
from mainapp.service.ProductType import ProductTypeService, ProductColorService, ProductSizeService
from mainapp.Common import ConstValiable
from mainapp.model.ProductDetail import ProductDetail
from mainapp.model.Product import Product

@login_required(login_url='/login/')
def view_all_product_page(request):
    """
    View all product - need auth
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
    View product detail page - need auth
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
            list_p_promotion_is_running = ProductPromotionService.get_all_promotion_is_running_in_product_id(product.product_id)
            list_p_promotion_is_coming = ProductPromotionService.get_all_promotion_is_coming_in_product_id(product.product_id)
            list_p_promotion_is_passed = ProductPromotionService.get_all_promotion_is_passed_in_product_id(product.product_id)

            context = {
                'product': product,
                'list_product_detail': list_p_detail,
                'list_product_image': list_p_image,
                'list_p_promotion_is_running': list_p_promotion_is_running,
                'list_p_promotion_is_coming': list_p_promotion_is_coming,
                'list_p_promotion_is_passed': list_p_promotion_is_passed,
            }
            return render(request, 'private/Product/productdetail.html', context=context)
        else:
            raise Exception('Product not exist')
    except Exception as error:
        print(error)
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/products/')

@login_required(login_url='/login/')
def view_update_product_detail_form_page(request, product_id):
    """
    Page update product detail - need auth
    """
    try:
        # Get base info product       
        product = ProductService.get_product_detail_by_id(product_id)
        if product is not None:
            # Get list detail info product
            list_p_detail = ProductDetailService.get_all_detail_product_by_product_id(product.product_id)
            
            # Get list size
            list_p_size = ProductSizeService.get_all_product_size_in_product_type(product.product_type_id.product_type_id)

            # Get list color
            list_p_color = ProductColorService.get_all_product_color_in_type(product.product_type_id.product_type_id)

            context = {
                'product': product,
                'list_product_detail': list_p_detail,
                'list_p_size': list_p_size,
                'list_p_color': list_p_color
            }
            return render(request, 'private/Product/productdetailform.html', context=context)
        else:
            raise Exception('Product not exist')
    except Exception as error:
        print(error)
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/products/')

@login_required(login_url='/login/')
def view_insert_product_detail_form_page(request, product_type_id):
    """
    Page insert product detail - need auth
    """
    try:
        # Get product type       
        product_type = ProductTypeService.get_product_type_detail_by_id(product_type_id)
        if product_type is not None:
            
            # Get list size
            list_p_size = ProductSizeService.get_all_product_size_in_product_type(product_type_id)

            # Get list color
            list_p_color = ProductColorService.get_all_product_color_in_type(product_type_id)

            context = {
                'product_type': product_type,
                'list_p_size': list_p_size,
                'list_p_color': list_p_color
            }
            return render(request, 'private/Product/productdetailform.html', context=context)
        else:
            raise Exception('Product not exist')
    except Exception as error:
        print(error)
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/products/')

@login_required(login_url='/login/')
def insert_product_and_product_detail(request, product_type_id):
    """
    Insert product and product detail - need auth
    """
    try:
        if request.method == 'POST':
            # Get product type       
            product_type = ProductTypeService.get_product_type_detail_by_id(product_type_id)
            if product_type is not None:
                # Get list size
                list_p_size = ProductSizeService.get_all_product_size_in_product_type(product_type_id)

                # Get list color
                list_p_color = ProductColorService.get_all_product_color_in_type(product_type_id)

                # Get data in request
                product_code = request.POST.get('product-code')
                product_name = request.POST.get('product-name')
                product_description = request.POST.get('product-description')
                product_detail = request.POST.get('product-detail')
                number_item_detail = request.POST.get('number-item-detail')
                color = request.POST.getlist('color')
                size = request.POST.getlist('size')
                number_of_product = request.POST.getlist('number-of-product')
                product_original_price = request.POST.getlist('product-original-price')
                product_public_price = request.POST.getlist('product-public-price')
                product_in_stock = request.POST.getlist('product-in-stock')

                # Make full list data
                color = get_item_in_detail(number_item_detail, color)
                size = get_item_in_detail(number_item_detail, size)
                number_of_product = get_item_in_detail(number_item_detail, number_of_product)
                product_original_price = get_item_in_detail(number_item_detail, product_original_price)
                product_public_price = get_item_in_detail(number_item_detail, product_public_price)
                product_in_stock = get_item_in_detail(number_item_detail, product_in_stock)

                list_product_detail = []
                for index in range(int(number_item_detail)):
                    product = Product(product_code=product_code,
                                        product_name=product_name,
                                        product_description=product_description,
                                        product_detail=product_detail,
                                        product_type_id_id=product_type_id)
                    detail = ProductDetail(number_of_product=number_of_product[index],
                                            product_original_price=product_original_price[index],
                                            product_public_price=product_public_price[index],
                                            product_color_id_id=color[index],
                                            product_size_id_id=size[index])
                    list_product_detail.append(detail)
                context = {
                    'product': product,
                    'list_product_detail': list_product_detail,
                    'product_type': product_type,
                    'list_p_size': list_p_size,
                    'list_p_color': list_p_color
                }
                check = validate_list_data(product_code, product_name, product_description, 
                                            color, size, number_of_product, 
                                            product_original_price, product_public_price, product_in_stock)
                print('controller check=' + str(check))
                if check:
                    print('befor insert')
                    # Insert
                    ProductService.insert_product_and_detail(product, list_product_detail)
                    messages.success(request, ConstValiable.MESSAGE_POPUP_SUCCESS)

                    return redirect('/products/' + str())
                else:
                    messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
                    return render(request, 'private/Product/productdetailform.html', context=context)
            else:
                raise Exception('Product not exist')
    except Exception as error:
        print(error)
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/products/')

@login_required(login_url='/login/')
def update_product_and_product_detail(request, product_id, product_type_id):
    """
    Update product and product detail - need auth
    """
    try:
        if request.method == 'POST':
            # Get product type       
            product_type = ProductTypeService.get_product_type_detail_by_id(product_type_id)
            if product_type is not None:
                # Get list size
                list_p_size = ProductSizeService.get_all_product_size_in_product_type(product_type_id)

                # Get list color
                list_p_color = ProductColorService.get_all_product_color_in_type(product_type_id)

                # Get data in request
                product_code = request.POST.get('product-code').strip()
                product_name = request.POST.get('product-name').strip()
                product_description = request.POST.get('product-description').strip()
                product_detail = request.POST.get('product-detail').strip()
                number_item_detail = request.POST.get('number-item-detail')
                color = request.POST.getlist('color')
                size = request.POST.getlist('size')
                number_of_product = request.POST.getlist('number-of-product')
                product_original_price = request.POST.getlist('product-original-price')
                product_public_price = request.POST.getlist('product-public-price')
                product_in_stock = request.POST.getlist('product-in-stock')
                product_detail_id = request.POST.getlist('product-detail-id')

                # Make full list data
                color = get_item_in_detail(number_item_detail, color)
                size = get_item_in_detail(number_item_detail, size)
                number_of_product = get_item_in_detail(number_item_detail, number_of_product)
                product_original_price = get_item_in_detail(number_item_detail, product_original_price)
                product_public_price = get_item_in_detail(number_item_detail, product_public_price)
                product_in_stock = get_item_in_detail(number_item_detail, product_in_stock)
                product_detail_id = get_item_in_detail(number_item_detail, product_detail_id)

                list_product_detail = []
                product = Product(product_id=product_id,
                                product_code=product_code,
                                product_name=product_name,
                                product_description=product_description,
                                product_detail=product_detail,
                                product_type_id_id=product_type_id)
                for index in range(int(number_item_detail)):
                    detail = ProductDetail(product_detail_id=product_detail_id[index],
                                            number_of_product=number_of_product[index],
                                            product_original_price=product_original_price[index],
                                            product_public_price=product_public_price[index],
                                            product_color_id_id=color[index],
                                            product_size_id_id=size[index],
                                            product_in_stock=product_in_stock[index],
                                            product_id_id=product_id)
                    list_product_detail.append(detail)
                context = {
                    'product': product,
                    'list_product_detail': list_product_detail,
                    'product_type': product_type,
                    'list_p_size': list_p_size,
                    'list_p_color': list_p_color
                }
                check = validate_list_data(product_code, product_name, product_description, 
                                            color, size, number_of_product, 
                                            product_original_price, product_public_price, product_in_stock)
                print('controller check=' + str(check))
                if check:
                    # Update
                    ProductService.update_product_and_detail(product, list_product_detail)
                    messages.success(request, ConstValiable.MESSAGE_POPUP_SUCCESS)

                    return redirect('/products/' + str(product_id))
                else:
                    messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
                    return render(request, 'private/Product/productdetailform.html', context=context)
            else:
                raise Exception('Product not exist')
    except Exception as error:
        print(error)
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/products/')

@login_required(login_url='/login/')
def view_modify_product_image_page(request, product_id):
    """
    View detail, insert, delete product image page - need auth
    """
    try:
        # Get base info product       
        product = ProductService.get_product_detail_by_id(product_id)
        if product is not None:
            # Get list image of product
            list_p_image = ProductImageService.get_all_product_image_by_product_id(product.product_id)

            context = {
                'product': product,
                'list_product_image': list_p_image,
            }
            return render(request, 'private/Product/productimagedetail.html', context=context)
        else:
            raise Exception('Product not exist')
    except Exception as error:
        print(error)
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/products/')

def get_item_in_detail(number_item_detail, item):
    """
    get item in list data
    """
    number = int(number_item_detail) - len(item)
    if number > 0:
        for i in range(number):
            item.append(-1)
    return item

def validate_list_data(product_code, product_name, product_description, 
                        color, size, number_of_product, 
                        product_original_price, product_public_price, product_in_stock):
    """
    Validate data
    """
    print('val 1')
    if len(str(product_code)) > 25 or len(str(product_name)) > 255 or len(str(product_description)) > 1000:
        print(0)
        return False
    for n in color:
        if int(n) <= 0:
            print(1)
            return False
    
    for n in size:
        if int(n) <= 0:
            print(2)
            return False
    for n in number_of_product:
        if int(n) < 0:
            print(3)
            return False
    for n in product_original_price:
        if Decimal(n) < 0:
            print(4)
            return False
    for n in product_public_price:
        if Decimal(n) < 0:
            print(5)
            return False
    for n in product_in_stock:
        if int(n) < 0:
            print(6)
            return False
    
    return True
    