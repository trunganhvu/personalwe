from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
import json
from django.conf import settings
from django.core.cache import cache

LOAD_ADDRESS_FILE = 'load-address-file'

def load_address_file():
    """
    Read file json
    """
    # Check exist in cache
    cached_data = cache.get(LOAD_ADDRESS_FILE)
    if not cached_data:
        file = open('address.json')
        data = json.load(file)

        # Set into cache
        cache.set(LOAD_ADDRESS_FILE, data, settings.CACHE_TIME)
        cached_data = data
    return cached_data

@api_view(['GET'])
def get_all_city(request):
    """
    API get all city
    """
    # Get all data
    data = load_address_file()

    list_city = []

    for da in data:
        city = {
            'name': da['name'],
            'code': da['code']
        }
        list_city.append(city)
    return Response(list_city)

@api_view(['GET'])
def get_all_districts_in_city(request, city_code):
    """
    Get all districts in city
    """
    # Get all data
    data = load_address_file()

    list_district = []

    # Loop all data
    for da in data:
        # If is city
        if da['code'] == city_code:
            districts = da['districts']

            # Get all district 
            for district in districts:
                d = {
                    'name': district['name'],
                    'code': district['code'],
                }
                list_district.append(d)
            break
    return Response(list_district)

@api_view(['GET'])
def get_all_wards_in_city(request, city_code, district_code):
    """
    Get all wards in city
    """
    # Get all data
    data = load_address_file()

    list_ward = []

    # Loop all data
    for da in data:
        # If is city
        if da['code'] == city_code:
            districts = da['districts']

            # Get all district 
            for district in districts:

                if district['code'] == district_code:
                    wards = district['wards'] 
                    for ward in wards:
                        w = {
                            'name': ward['name'],
                            'code': ward['code']
                        }
                        list_ward.append(w)
                break
        break
    return Response(list_ward)

