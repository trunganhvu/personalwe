from mainapp.model.Event import Event
from datetime import datetime
from django.core.cache import cache
from mainapp.Common import CacheUtil
from django.conf import settings
from django.utils import timezone

KEY_CACHE_DAO_GET_ALL_EVENT_ACTIVE = 'context-dao-all-event-active'
KEY_CACHE_DAO_GET_ALL_EVENT_NOT_ACTIVE = 'context-dao-all-event-not-active'

def get_all_event_not_active():
    """
    Get all event active
    """
    list_event = Event.objects.filter(active=False)
    return list_event

def get_all_event_active():
    """
    Get all event active
    """
    list_event = Event.objects.filter(active=True)

    return list_event

def get_all_event_active_running():
    """
    Get all event running
    """
    # Get current date
    now = datetime.now(tz=timezone.utc)

    list_event = Event.objects.filter(active=True, event_start__lte=now, event_end__gte=now)
    return list_event

def get_all_event_active_is_comming():
    """
    Get all event is comming
    """
    # Get current date
    now = datetime.now(tz=timezone.utc)

    list_event = Event.objects.filter(active=True, event_start__gte=now, event_end__gte=now)
    return list_event

def get_all_event_active_is_passed():
    """
    Get all event is passed
    """
    # Get current date
    now = datetime.now(tz=timezone.utc)

    list_event = Event.objects.filter(active=True, event_start__lte=now, event_end__lte=now)
    return list_event

def get_event_detail_by_id(event_id):
    """
    Get event detail by id
    """
    event = Event.objects.get(pk=event_id)
    return event

def insert_event(event):
    """
    Insert event
    """
    e = Event(event_name=event.event_name,
            event_note=event.event_note,
            event_slogun=event.event_slogun,
            event_description=event.event_description,
            event_image_banner_name=event.event_image_banner_name,
            event_image_banner_path=event.event_image_banner_path,
            active=event.active,
            event_start=event.event_start,
            event_end=event.event_end,
            created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    e.save()
    return e

def update_event(event):
    """
    Update event
    """
    e = Event.objects.get(pk=event.event_id)
    e.event_name = event.event_name
    e.event_note = event.event_note
    e.event_slogun = event.event_slogun
    e.event_description = event.event_description
    e.event_image_banner_name = event.event_image_banner_name
    e.event_image_banner_path = event.event_image_banner_path
    e.active = event.active
    e.event_start = event.event_start
    e.event_end = event.event_end
    e.save()
    return e

def delete_event(event_id):
    """
    Delete event by id
    """
    e = Event.objects.get(pk=event_id)
    e.delete()