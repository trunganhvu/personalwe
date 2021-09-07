from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from mainapp.service.Header import BannerTitleService
from django.utils.safestring import mark_safe
from django.contrib import messages
from mainapp.Common import ConstValiable
from django.contrib.auth.decorators import login_required

@api_view(['GET'])
def get_banner_title(request):
    """
    API get banner title
    """
    context = BannerTitleService.get_banner_title()
    return Response(context)

@login_required(login_url='/login/')
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
                messages.success(request, ConstValiable.MESSAGE_POPUP_SUCCESS)
            else:
                # Message error
                messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        except Exception:
            messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/header')

