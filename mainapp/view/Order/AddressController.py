from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
import json
from django.conf import settings
from django.core.cache import cache

LOAD_ADDRESS_FILE = 'load-address-file'
GET_ALL_CITY = 'get-all-city' 
GET_ALL_DISTRICTS_IN_CITY = 'get-all-districts-in-city-' 
GET_ALL_WARDS_IN_CITY = 'get-all-wards-in-city-'


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
    # Check exist in cache
    cached_data = cache.get(GET_ALL_CITY)
    if not cached_data:
        # Get all data
        data = load_address_file()

        list_city = []

        for da in data:
            city = {
                'name': da['name'],
                'code': da['code']
            }
            list_city.append(city)

        # Set into cache
        cache.set(GET_ALL_CITY, list_city, settings.CACHE_TIME)
        cached_data = list_city
    
    return Response(cached_data)

def get_all_city2():
    """
    Getl all city 
    """
    # Check exist in cache
    cached_data = cache.get(GET_ALL_CITY)
    if not cached_data:
        # Get all data
        data = load_address_file()

        list_city = []

        for da in data:
            city = {
                'name': da['name'],
                'code': da['code']
            }
            list_city.append(city)

        # Set into cache
        cache.set(GET_ALL_CITY, list_city, settings.CACHE_TIME)
        cached_data = list_city
    return cached_data

@api_view(['GET'])
def get_all_districts_in_city(request, city_code):
    """
    Get all districts in city
    """
    # Check exist in cache
    key_cache = GET_ALL_DISTRICTS_IN_CITY + str(city_code)
    cached_data = cache.get(key_cache)
    if not cached_data:
        # Get all data
        data = load_address_file()
        list_district = []

        # Loop all data
        for da in data:
            # If is city
            if da['code'] == city_code:
                districts = da['districts']
                # # Get all district 
                for district in districts:
                    # print(district)
                    d = {
                        'name': district['name'],
                        'code': district['code'],
                    }
                    list_district.append(d)
                # print(list_district)
                break
        # Set into cache
        cache.set(key_cache, list_district, settings.CACHE_TIME)
        cached_data = list_district
    return Response(cached_data)

@api_view(['GET'])
def get_all_wards_in_city(request, city_code, district_code):
    """
    Get all wards in city
    """
    # Check exist in cache
    key_cache = GET_ALL_WARDS_IN_CITY + str(city_code) + '-' + str(district_code)
    cached_data = cache.get(key_cache)
    if not cached_data:
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
        # Set into cache
        cache.set(key_cache, list_ward, settings.CACHE_TIME)
        cached_data = list_ward
    return Response(cached_data)

