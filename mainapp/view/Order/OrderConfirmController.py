from mainapp.model.Product import Product
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from mainapp.service.Cart import CartService
from mainapp.service.Product import ProductDetailService, ProductService, ProductImageService
from mainapp.service.ProductType import ProductTypeService
from mainapp.view.Order import AddressController
from mainapp.Common import DateTime
import math, json
from django.core import serializers
from collections import namedtuple

def view_confirm_order(request):
    """
    View page confirm order
    """
    try:
        if request.method == 'POST':
            key_current_time = request.POST.get('key_current_time')
            context_session = []
            if key_current_time in request.session:
                context_session = request.session[key_current_time]

                # Detail user form
                full_name = request.POST.get('full-name')
                phone_number = request.POST.get('phone-number')
                email = request.POST.get('email')
                city = request.POST.get('city')
                district = request.POST.get('district')
                address_detail = request.POST.get('address-detail')
                note = request.POST.get('note')
                payment = request.POST.get('payment')

                list_product_item = []
                list_product_item_cart = context_session['list_product_item_cart']
                for item in list_product_item_cart:
                    # Product base
                    product_id = item['product']
                    product = ProductService.get_product_detail_by_id(product_id)

                    # Product detail
                    product_detail_id = item['product_detail']
                    product_detail = ProductDetailService.get_product_detail_by_product_detail_id(product_detail_id)

                    # Product size
                    product_size_id = item['product_size']
                    product_size = product_detail.product_size_id

                    # Product color
                    product_color_id = item['product_color']
                    product_color = product_detail.product_color_id

                    # Quantity
                    quantity = item['quantity']

                    # Product image
                    product_image_id = item['product_image']
                    product_image = ProductImageService.get_product_image_by_image_id(product_image_id)

                    # Price
                    total_price_item = item['total_price_item']
                    product_item = {
                        'product': product,
                        'product_detail': product_detail,
                        'product_size': product_size,
                        'product_color': product_color,
                        'quantity': quantity,
                        'product_image': product_image,
                        'total_price_item': total_price_item,
                    }
                    list_product_item.append(product_item)
                context = {
                    'list_product_item_cart': list_product_item,
                    'total_bill': context_session['total_bill'],
                    'full_name': full_name,
                    'phone_number': phone_number,
                    'email': email,
                    'city': city,
                    'district': district,
                    'address_detail': address_detail,
                    'note': note,
                    'payment': payment,
                }
            return render(request, 'public/Order/orderconfirm.html', context=context)
            
        else:
            raise Exception
    except Exception as error:
        print(error)
        return redirect('/shop/')