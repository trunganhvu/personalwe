from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from mainapp.service.Header import HeaderService
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.utils.safestring import mark_safe
from django.contrib import messages

# @cache_page(settings.CACHE_TIME, key_prefix='api-header')
@api_view(['GET'])
def get_header_path(request):
    """
    Get path header
    """
    if request.method == 'GET':
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
            if header_name != '' and header_image != None:
                header_name = str(mark_safe(header_name)).strip()
                url = HeaderService.insert_header_image(header_image, header_name)
                print(url)
                messages.success(request, "Thành công.")
            else:
                # Message error
                print()
                messages.error(request, "Thất bại.")
        except Exception:
            messages.error(request, "Thất bại.")
        return redirect('/header')

