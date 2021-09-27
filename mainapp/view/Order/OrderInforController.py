from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from mainapp.service.Cart import CartService
from mainapp.service.Product import ProductDetailService, ProductService, ProductImageService
from mainapp.service.ProductType import ProductTypeService
from mainapp.view.Order import AddressController
import math

def view_info_order(request):
    """
    View form order info
    """
    try:
        if request.method == 'POST':
            # Get data in form
            cart_detail_id = request.POST.getlist('cart-detail-id')

            list_product_item_cart = []
            list_city = []
            total_bill = 0
            uc_code = request.COOKIES['uc_code']

            # check key code exist
            cart = CartService.get_cart_by_key_code(uc_code)
            if cart is not None:
                # list city
                list_city = AddressController.get_all_city2()
                for detail_id in cart_detail_id:
                    c_detail = CartService.get_cart_detail_by_cart_detail_id(detail_id)

                    if c_detail is not None:
                        product = c_detail.product_detail_id.product_id

                        product_detail = c_detail.product_detail_id
                        product_detail.product_public_price = math.floor(product_detail.product_public_price)

                        product_size = c_detail.product_detail_id.product_size_id

                        product_color = c_detail.product_detail_id.product_color_id

                        product_image = ProductImageService.get_one_product_image_by_product_id(product.product_id)

                        total_price_item = product_detail.product_public_price * c_detail.quantity
                        total_bill += total_price_item
                        product_item = {
                            'product': product,
                            'product_detail': product_detail,
                            'product_size': product_size,
                            'product_color': product_color,
                            'quantity': c_detail.quantity,
                            'product_image': product_image,
                            'total_price_item': total_price_item,
                        }
                        list_product_item_cart.append(product_item)
            context = {
                'list_product_item_cart': list_product_item_cart,
                'list_city': list_city,
                'total_bill': total_bill,
            }
            return render(request, 'public/Order/orderinfor.html', context=context)
        else:
            raise Exception
    except Exception as error:
        return redirect('/shop/')