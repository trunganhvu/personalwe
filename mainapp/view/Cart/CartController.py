from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect

from mainapp.Common import ConstValiable
from django.contrib.auth.decorators import login_required
from mainapp.service.Cart import CartService
from mainapp.service.Product import ProductDetailService, ProductService

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
            # product_detail = ProductDetailService.get_product_detail_by_product_detail_id()
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