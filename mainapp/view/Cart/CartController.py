from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect

from mainapp.Common import ConstValiable
from django.contrib.auth.decorators import login_required
from mainapp.service.Cart import CartService
from mainapp.service.Product import ProductDetailService, ProductService, ProductImageService
from mainapp.service.ProductType import ProductTypeService
import math

@api_view(['GET'])
def count_item_in_cart_by_key(request, key):
    """
    API get total item in cart
    """
    context = CartService.count_cart_item_by_key_code(key)
    return Response(context)

def view_detail_cart_page(request):
    """
    View page detatil cart
    """
    try:
        list_product_type = ProductTypeService.get_all_product_type()
        uc_code = request.COOKIES['uc_code']
        list_product = []
        # Get list item
        list_item = CartService.get_cart_item_by_key_code(uc_code)
        if list_item is not None:
            for item in list_item:
                # Product
                product = item.product_detail_id.product_id

                # Image
                product_image = ProductImageService.get_one_product_image_by_product_id(product.product_id)
                
                # Product price
                price = math.floor(item.product_detail_id.product_public_price)

                item_product = {
                    'product': product,
                    'quantity': item.quantity,
                    'size': item.product_detail_id.product_size_id,
                    'color': item.product_detail_id.product_color_id,
                    'product_image': product_image,
                    'price': f'{price:,}',
                    'product_detail': item.product_detail_id,
                }
                list_product.append(item_product)
        context = {
            'list_product': list_product,
            'list_product_type': list_product_type,
        }
        return render(request, 'public/Cart/Cart.html', context=context)
    except Exception as error:
        return redirect('/shop/')

def insert_item_into_cart(request, product_id):
    """
    Insert into cart
    """
    try:
        if request.method == 'POST':
            cart_product_id = request.POST.get('add-cart-product')
            cart_size = request.POST.get('add-cart-size')
            cart_color = request.POST.get('add-cart-color')
            cart_cookie_key = request.POST.get('add-cart-cookie-key')
            cart_quantity = request.POST.get('add-cart-quantity')
            if str(cart_product_id) != str(product_id):
                raise Exception('Product id not match')

            # Check product exist
            product = ProductService.get_product_detail_by_id(product_id)
            if product is None:
                raise Exception('Product is not exist')

            # Check product detail exist
            product_detail = ProductDetailService.get_product_detail_by_product_id_size_id_color_id(cart_product_id,
                                                                                                    cart_size,
                                                                                                    cart_color)
            if product_detail is None:
                raise Exception('Product detail is not exist')
            
            if product_detail.product_in_stock < int(cart_quantity):
                raise Exception('Quantity in stock not enough')

            # Insert to cart
            CartService.insert_cart_and_item(product_detail.product_detail_id,
                                            cart_quantity,
                                            cart_cookie_key)

            return redirect('/shop/product/' + str(product_id))

    except Exception as error:
        print(error)
        return redirect('/shop/product/' + str(product_id))

def update_item_in_cart(request):
    """
    Update item in cart
    """

def delete_item_in_cart(request):
    """
    Delete item in cart
    """