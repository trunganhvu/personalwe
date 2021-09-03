from mainapp.model.Category import Category
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
            category = Category(category_name=category_name,
                                category_url=category_url,
                                display=category_display,
                                display_order=category_display_order,
                                category_image_default_name=category_image_name,
                                category_image_default=category_image)
            context = {
                'category': category
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
            return render(request, 'private/Category/categoryform.html')
        return redirect('/category')

def get_category_detail_page(request, id):
    """
    Get detail category
    """
    context = {}
    try:
        category = CategoryService.get_category_detail(id)
        context = {
            'category': category
        }
    except Exception:
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/category')
    return render(request, 'private/Category/categorydetail.html', context=context)

def view_category_form_update_page(request, id):
    """
    View form update category
    """
    context = {}
    try:
        category = CategoryService.get_category_detail(id)
        context = {
            'category': category
        }
    except Exception:
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/category')
    return render(request, 'private/Category/categoryform.html', context=context)

def update_category_form(request, id):
    """
    Update category by id
    """
    if request.method == 'POST':
        try:
            # Get data in form
            category_id = request.POST.get('category-id')
            category_name = request.POST.get('category-name')
            category_url = request.POST.get('category-url')
            category_image_name = request.POST.get('category-image-name')
            if 'category-image' in request.FILES:
                category_image = request.FILES['category-image']
            else:
                category_image = ''
            category_display = request.POST.get('category-display')
            category_display_order = request.POST.get('category-display-order')
            category_image_now = request.POST.get('category-image-now')
            if category_image == '':
                is_update_image = False
                category_image = category_image_now
            else:
                is_update_image = True
            category = Category(category_id=category_id,
                                category_name=category_name,
                                category_url=category_url,
                                display=category_display,
                                display_order=category_display_order,
                                category_image_default_name=category_image_name,
                                category_image_default=category_image)
            context = {
                'category': category
            }
            check = validate_form_insert(category_name, category_url, category_image_name, category_image, category_display, category_display_order, is_update_image)
            if category_id == id and check:
                print('validate true')
                # update
                CategoryService.update_category(category, is_update_image)
                messages.success(request, ConstValiable.MESSAGE_POPUP_SUCCESS)
            else:
                print(category.category_name)
                messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
                return render(request, 'private/Category/categoryform.html', context=context)
        except Exception:
            messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
            return redirect('/category-form/' + str(id))
        return redirect('/category')

def get_category_display(request):
    """
    Get all category display
    """
    
def validate_form_insert(category_name, category_url, category_image_name, category_image, category_display, category_display_order, is_update_image):
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
    if is_update_image:
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
