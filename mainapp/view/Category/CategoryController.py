from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from mainapp.service.Category import CategoryService
from django.utils.safestring import mark_safe
from django.contrib import messages
from mainapp.Common import ConstValiable

# @api_view(['GET'])
# def get_banner_title(request):
#     """
#     API get banner title
#     """
#     context = BannerTitleService.get_banner_title()
#     return Response(context)

def view_category_page(request):
    """
    View page category
    """
    category_list = CategoryService.get_all_category()
    context = {
        'categorys': category_list
    }
    print(context)
    return render(request, 'private/Category/category.html', context)

def view_category_form_page(request):
    """
    View form update, insert category
    """
    return render(request, 'private/Category/categoryform.html')


