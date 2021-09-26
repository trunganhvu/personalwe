from django.shortcuts import render, redirect

from mainapp.Common import ConstValiable
from django.contrib.auth.decorators import login_required
from mainapp.service.Cart import CartService
from mainapp.service.Product import ProductDetailService, ProductService, ProductImageService
from mainapp.service.ProductType import ProductTypeService

def view_info_order(request):
    """
    View form order info
    """
    try:
        if request.method == 'POST':
            # Get data in form
            cart_detail_id = request.POST.getlist('cart-detail-id')

            list_product_item_cart = []
            uc_code = request.COOKIES['uc_code']

            # check key code exist
            cart = CartService.get_cart_by_key_code(uc_code)
            if cart is not None:
                for detail_id in cart_detail_id:
                    c_detail = CartService.get_cart_detail_by_cart_detail_id(detail_id)

                    if c_detail is not None:
                        product = c_detail.product_detail_id.product_id

                        product_detail = c_detail.product_detail_id

                        product_size = c_detail.product_detail_id.product_size_id

                        product_color = c_detail.product_detail_id.product_color_id

                        product_item = {
                            'product': product,
                            'product_detail': product_detail,
                            'product_size': product_size,
                            'product_color': product_color,
                            'quantity': c_detail.quantity,
                        }
                        list_product_item_cart.append(product_item)
            context = {
                'list_product_item_cart': list_product_item_cart
            }
            return render(request, 'public/Order/orderinfor.html', context=context)
        else:
            raise Exception
    except Exception as error:
        return redirect('/shop/')