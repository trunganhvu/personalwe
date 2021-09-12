from django.core.cache import cache
from mainapp.Common import CacheUtil
from django.conf import settings

from mainapp.dao.Event import EventDao
from mainapp.Common import Util
KEY_CACHE_GET_ALL_EVENT_ACTIVE = 'context-all-event-active'
KEY_CACHE_GET_ALL_EVENT_NOT_ACTIVE = 'context-all-event-not-active'
KEY_CACHE_GET_ALL_EVENT_ACTIVE_RUNNING = 'context-all-event-active-running'
KEY_CACHE_GET_ALL_EVENT_ACTIVE_IS_COMMING = 'context-all-event-active-is-comming'
KEY_CACHE_GET_ALL_EVENT_ACTIVE_PASSED = 'context-all-event-active-passed'
KEY_CACHE_GET_EVENT_DETAIL_ID = 'context-event-detail-id-'


def get_all_event_active():
    """
    Get all event active
    """
    cached_data = cache.get(KEY_CACHE_GET_ALL_EVENT_ACTIVE)
    if not cached_data:
        # Get all in DB
        list_event = EventDao.get_all_event_active()

        if list_event.count() > 0:
            # Set into cache
            cache.set(KEY_CACHE_GET_ALL_EVENT_ACTIVE, list_event, settings.CACHE_TIME)
            cached_data = list_event 
    return cached_data

def get_all_event_not_active():
    """
    Get all event active
    """
    cached_data = cache.get(KEY_CACHE_GET_ALL_EVENT_NOT_ACTIVE)
    if not cached_data:
        # Get all in DB
        list_event = EventDao.get_all_event_not_active()

        if list_event.count() > 0:
            # Set into cache
            cache.set(KEY_CACHE_GET_ALL_EVENT_NOT_ACTIVE, list_event, settings.CACHE_TIME)
            cached_data = list_event 
    return cached_data

def get_all_event_active_running():
    """
    Get all event running
    """
    cached_data = cache.get(KEY_CACHE_GET_ALL_EVENT_ACTIVE_RUNNING)
    if not cached_data:
        # Get all in DB
        list_event = EventDao.get_all_event_active_running()

        if list_event.count() > 0:
            # Set into cache
            cache.set(KEY_CACHE_GET_ALL_EVENT_ACTIVE_RUNNING, list_event, settings.CACHE_TIME)
            cached_data = list_event 
    return cached_data

def get_all_event_active_is_comming():
    """
    Get all event is comming
    """
    cached_data = cache.get(KEY_CACHE_GET_ALL_EVENT_ACTIVE_IS_COMMING)
    if not cached_data:
        # Get all in DB
        list_event = EventDao.get_all_event_active_is_comming()

        if list_event.count() > 0:
            # Set into cache
            cache.set(KEY_CACHE_GET_ALL_EVENT_ACTIVE_IS_COMMING, list_event, settings.CACHE_TIME)
            cached_data = list_event 
    return cached_data

def get_all_event_active_is_passed():
    """
    Get all event is passed
    """
    cached_data = cache.get(KEY_CACHE_GET_ALL_EVENT_ACTIVE_PASSED)
    if not cached_data:
        # Get all in DB
        list_event = EventDao.get_all_event_active_is_passed()

        if list_event.count() > 0:
            # Set into cache
            cache.set(KEY_CACHE_GET_ALL_EVENT_ACTIVE_PASSED, list_event, settings.CACHE_TIME)
            cached_data = list_event 
    return cached_data

def get_event_detail_by_id(event_id):
    """
    Get event detail by id
    """
    key_cache = KEY_CACHE_GET_EVENT_DETAIL_ID + str(event_id)
    cached_data = cache.get(key_cache)
    if not cached_data:
        # Get all in DB
        event = EventDao.get_event_detail_by_id(event_id)

        if event is not None:
            # Set into cache
            cache.set(key_cache, event, settings.CACHE_TIME)
            cached_data = event 
    return cached_data

def insert_event(event):
    """
    Insert event
    """
    full_path_image = ''
    try:
        # Save image
        full_path_image = Util.save_image_to_media(event.event_image_banner_path,
                                                    event.event_image_banner_name)
        event.event_image_banner_path = full_path_image

        # Change display
        event.active = True if event.active == 'true' else False

        # Insert to DB
        e = EventDao.insert_event(event)

        # Set cache
        key_cache_detail = KEY_CACHE_GET_EVENT_DETAIL_ID + str(e.event_id)
        CacheUtil.clean_cache_by_key(key_cache_detail)
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_EVENT_ACTIVE)
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_EVENT_ACTIVE_RUNNING)
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_EVENT_ACTIVE_IS_COMMING)
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_EVENT_ACTIVE_PASSED)
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_EVENT_NOT_ACTIVE)

        cache.set(key_cache_detail, e, settings.CACHE_TIME)
    except Exception as error:
        # Delete image
        print(error)
        if full_path_image != '':
            Util.delete_image_in_media(full_path_image)

        raise error

def update_event(event, is_update_image):
    """
    Update event
    """
    full_path_image = ''
    try:
        if is_update_image:
            # Save image
            full_path_image = Util.save_image_to_media(event.event_image_banner_path,
                                                        event.event_image_banner_name)
            event.event_image_banner_path = full_path_image
            
        # Change display
        event.active = True if event.active == 'true' else False

        # Update to DB
        e = EventDao.update_event(event)

        # Set cache
        key_cache_detail = KEY_CACHE_GET_EVENT_DETAIL_ID + str(e.event_id)
        CacheUtil.clean_cache_by_key(key_cache_detail)
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_EVENT_ACTIVE)
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_EVENT_ACTIVE_RUNNING)
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_EVENT_ACTIVE_IS_COMMING)
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_EVENT_ACTIVE_PASSED)
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_EVENT_NOT_ACTIVE)

        cache.set(key_cache_detail, e, settings.CACHE_TIME)
    except Exception as error:
        # Delete image
        if full_path_image != '':
            Util.delete_image_in_media(full_path_image)
        raise error

def delete_event(event_id):
    """
    Delete event by id
    """
    event = get_event_detail_by_id(event_id)
    if event is not None:
        # Delete DB
        EventDao.delete_event(event_id)

        # Clean cache
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_EVENT_DETAIL_ID + str(event.event_id))
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_EVENT_ACTIVE)
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_EVENT_ACTIVE_RUNNING)
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_EVENT_ACTIVE_IS_COMMING)
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_EVENT_ACTIVE_PASSED)
        CacheUtil.clean_cache_by_key(KEY_CACHE_GET_ALL_EVENT_NOT_ACTIVE)
