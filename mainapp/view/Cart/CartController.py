from rest_framework.decorators import api_view
from rest_framework.response import Response

from mainapp.Common import ConstValiable
from django.contrib.auth.decorators import login_required
from mainapp.service.Cart import CartService

@api_view(['GET'])
def count_item_in_cart_by_key(request, key):
    """
    API get total item in cart
    """
    print('con 1')
    context = CartService.count_cart_item_by_key_code(key)
    return Response(context)