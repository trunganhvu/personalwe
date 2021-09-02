from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from mainapp.service.Header import HeaderService
from django.views.decorators.cache import cache_page
from django.utils.safestring import mark_safe
from django.contrib import messages
from mainapp.Common import ConstValiable

@api_view(['GET'])
def get_header_path(request):
    """
    Get path header
    """
    context = HeaderService.get_path_header()
    return Response(context)

def view_header_page(request):
    """
    View page manager header
    """
    return render(request, 'private/Header/header.html')

def insert_header_image_form(request):
    """
    Get data post to update header image
    """
    if request.method == 'POST':
        try:
            # Get data in from
            header_image = request.FILES["image-header"]
            header_name = request.POST.get('name-header')

            # Check none
            if validation_header(header_name, header_image):
                header_name = str(mark_safe(header_name)).strip()
                url = HeaderService.insert_header_image(header_image, header_name)
                print(url)
                messages.success(request, ConstValiable.MESSAGE_POPUP_SUCCESS)
            else:
                # Message error
                messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        except Exception:
            messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/header')

def validation_header(header_name, header_image):
    """
    Validate data header user input
    """
    if header_name != '' and header_image != None:
        if len(header_name) <= 100 and len(header_image) <= 255:
            return True
    return False
