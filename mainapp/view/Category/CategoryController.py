from django.conf import settings
from django.conf.urls import url
from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from mainapp.service.Category import CategoryService
from django.utils.safestring import mark_safe
from django.contrib import messages
from mainapp.Common import ConstValiable

import re, os

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
    print(os.path.exists('/home/trunganh/django-test/personalweb/static/media/images/1234.jpeg'))
    print(os.path.exists('/home/trunganh/django-test/personalweb/mainapp/static/media/images/222.jpeg'))
    return render(request, 'private/Category/categoryform.html')

def insert_category_form(request):
    """
    Insert new category
    """
    if request.method == 'POST':
        try:
            # Get data in form
            category_name = request.POST.get('category-name')
            category_url = request.POST.get('category-url')
            category_image_name = request.POST.get('category-image-name')
            category_image = request.FILES['category-image']
            category_display = request.POST.get('category-display')
            category_display_order = request.POST.get('category-display-order')
            context = {
                'category_name': category_name,
                'category_url': category_url,
                'category_image_name': category_image_name,
                'category_image': category_image,
                'category_display': category_display,
                'category_display_order': category_display_order
            }
            check = validate_form_insert(category_name, category_url, category_image_name, category_image, category_display, category_display_order)
            if check:
                CategoryService.insert_category(category_name, category_url, category_image_name, category_image, category_display, category_display_order)
                messages.success(request, ConstValiable.MESSAGE_POPUP_SUCCESS)
            else:
                messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
                return render(request, 'private/Category/categoryform.html', context=context)

        except Exception:
            messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
            return render(request, 'private/Category/categoryform.html', context=context)
        return redirect('/category')

def validate_form_insert(category_name, category_url, category_image_name, category_image, category_display, category_display_order):
    """
    Validate data form insert category
    """
    re_name = "^[A-Za-z0-9_ ]*$"
    re_url = "^[A-Za-z0-9_-]*$"
    # Check name
    if category_name is None or not re.match(re_name, category_name):
        return False
    # Check url
    if category_url is None or not re.match(re_url, category_url):
        return False
    # Check image name
    if category_image_name is None or not re.match(re_url, category_image_name):
        return False
    # Check image type
    image_split = category_image.name.split('.')
    image_type = image_split[-1]
    check = image_type in ['png', 'jpg', 'jpeg', 'tiff', 'bmp', 'gif', 'webp']
    if not check:
        return False
    # Check display
    if not category_display in ['true', 'false']:
        return False
    if category_display == 'true':
        if not category_display_order.isnumeric() or int(category_display_order) <= 0:
            return False
    
    return True
