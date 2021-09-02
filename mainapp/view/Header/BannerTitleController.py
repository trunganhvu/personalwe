import re
from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from mainapp.service.Header import BannerTitleService
from django.utils.safestring import mark_safe
from django.contrib import messages

@api_view(['GET'])
def get_banner_title(request):
    """
    API get banner title
    """
    context = BannerTitleService.get_banner_title()
    return Response(context)

def update_banner_title_form(request):
    """
    Get data post to update banner title
    """
    if request.method == 'POST':
        try:
            # Get data in from            
            title_banner = request.POST.get('title-banner')
            subtitle_banner = request.POST.get('subtitle-banner')

            # Check none
            if title_banner != '' and subtitle_banner != '':
                title_banner = str(mark_safe(title_banner)).strip()
                subtitle_banner = str(mark_safe(subtitle_banner)).strip()

                BannerTitleService.update_banner_title(title_banner, subtitle_banner)
                messages.success(request, "Thành công.")
            else:
                # Message error
                print()
                messages.error(request, "Thất bại.")
        except Exception:
            messages.error(request, "Thất bại.")
        return redirect('/header')

