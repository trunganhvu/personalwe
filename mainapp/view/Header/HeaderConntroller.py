from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from mainapp.service.Header import HeaderService

from django.views.decorators.cache import cache_page
from django.conf import settings

@cache_page(settings.CACHE_TIME)
@api_view(['GET'])
def get_header_path(request):
    """
    Get path header
    """
    if request.method == 'GET':
        context = HeaderService.get_path_header()
        return Response(context)