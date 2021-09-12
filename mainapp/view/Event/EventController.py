from mainapp.model.Event import Event
from django.conf import settings
from django.conf.urls import url
from django.shortcuts import render
from django.shortcuts import redirect
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from mainapp.service.Event import EventService
from mainapp.Common import ConstValiable

@login_required(login_url='/login/')
def view_all_event(request):
    """
    Get all event - need auth
    """
    list_event_running = EventService.get_all_event_active_running()
    list_event_is_comming = EventService.get_all_event_active_is_comming()
    list_event_passed = EventService.get_all_event_active_is_passed()
    list_event_not_active = EventService.get_all_event_not_active()

    context = {
        'list_event_running': list_event_running,
        'list_event_is_comming': list_event_is_comming,
        'list_event_passed': list_event_passed,
        'list_event_not_active': list_event_not_active
    }
    return render(request, 'private/Event/event.html', context)

@login_required(login_url='/login/')
def view_event_detail_by_id(request, event_id):
    """
    View event detail by id
    """
    try:
        print(event_id)
        event = EventService.get_event_detail_by_id(event_id)

        context = {
            'event': event,
        }
        return render(request, 'private/Event/eventdetail.html', context=context)
    except Exception:
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/product-type')


@login_required(login_url='/login/')
def view_event_insert_form_page(request):
    """
    View page insert event
    """
    return render(request, 'private/Event/eventform.html')


@login_required(login_url='/login/')
def view_event_update_form_page(request, event_id):
    """
    View page update event
    """
    try:
        event = EventService.get_event_detail_by_id(event_id)
        print(event.event_end)
        print(type(event.event_end))
        context = {
            'event': event
        }
        return render(request, 'private/Event/eventform.html', context=context)
    except Exception:
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/event/')

@login_required(login_url='/login/')
def insert_event(request):
    """
    Insert event
    """
    try:
        if request.method == 'POST':
            event_name = request.POST.get('event-name')
            event_slogun = request.POST.get('event-slogun')
            event_description = request.POST.get('event-description')
            event_note = request.POST.get('event-note')
            event_image_name = request.POST.get('event-image-name')
            if 'event-image' in request.FILES:
                event_image = request.FILES['event-image']
            else:
                event_image = ''
            event_start = request.POST.get('event-start')
            event_end = request.POST.get('event-end')
            active = request.POST.get('active')
            
            # Convert type str to date
            event_start = datetime.strptime(event_start, ConstValiable.FORMAT_DATE1)
            event_end = datetime.strptime(event_end, ConstValiable.FORMAT_DATE1)
            
            is_update_image = False

            event = Event(event_name=event_name.strip(),
                        event_slogun=event_slogun.strip(),
                        event_description=event_description.strip(),
                        event_note=event_note.strip(),
                        event_image_banner_name=event_image_name.strip(),
                        event_image_banner_path=event_image,
                        event_start=event_start,
                        event_end=event_end,
                        active=active)
            context = {
                'event': event
            }
            check = validate_event(event, is_update_image)
            if check:
                EventService.insert_event(event)
                messages.success(request, ConstValiable.MESSAGE_POPUP_SUCCESS)
                return redirect('/event/')
            else:
                messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
                return render(request, 'private/Event/eventform.html', context=context)

    except Exception as error:
        print(error)
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/event/')

@login_required(login_url='/login/')
def update_event(request, event_id):
    """
    Update event
    """
    try:
        if request.method == 'POST':
            event_id_hidden = request.POST.get('event-id')
            event_name = request.POST.get('event-name')
            event_slogun = request.POST.get('event-slogun')
            event_description = request.POST.get('event-description')
            event_note = request.POST.get('event-note')
            event_image_name = request.POST.get('event-image-name')
            event_image_now = request.POST.get('event-image-now')
            if 'event-image' in request.FILES:
                event_image = request.FILES['event-image']
                is_update_image = True
            else:
                event_image = event_image_now
                is_update_image = False
            event_start = request.POST.get('event-start')
            event_end = request.POST.get('event-end')
            active = request.POST.get('active')

            # Convert type str to date
            event_start = datetime.strptime(event_start, ConstValiable.FORMAT_DATE1)
            event_end = datetime.strptime(event_end, ConstValiable.FORMAT_DATE1)
            event = Event(event_id=event_id_hidden,
                        event_name=event_name.strip(),
                        event_slogun=event_slogun.strip(),
                        event_description=event_description.strip(),
                        event_note=event_note.strip(),
                        event_image_banner_name=event_image_name.strip(),
                        event_image_banner_path=event_image,
                        event_start=event_start,
                        event_end=event_end,
                        active=active)
            context = {
                'event': event
            }
            check = validate_event(event, is_update_image)
            if check:
                EventService.update_event(event, is_update_image)
                messages.success(request, ConstValiable.MESSAGE_POPUP_SUCCESS)
                return redirect('/event/' + str(event_id))
            else:
                messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
                return render(request, 'private/Event/eventform.html', context=context)

    except Exception as error:
        print(error)
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/event/')

@login_required(login_url='/login/')
def delete_event_by_id(request, event_id):
    """
    Delete event by id
    """
    try:
        EventService.delete_event(event_id)
        messages.success(request, ConstValiable.MESSAGE_POPUP_SUCCESS)
    
    except Exception:
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
    return redirect('/event/')


def validate_event(event, is_update_image):
    """
    Validation event
    """
    if event.event_name is None or len(event.event_name) > 255:
        return False
    if event.event_note is None or len(event.event_note) > 1000:
        return False
    if event.event_slogun is None or len(event.event_slogun) > 500:
        return False    
    if event.event_description is None or len(event.event_description) > 1000:
        return False
    if event.event_image_banner_name is None or len(event.event_image_banner_name) > 50:
        return False
    # Check image type
    if is_update_image:
        image_split = event.event_image_banner_path.name.split('.')
        image_type = image_split[-1]
        check = image_type.lower() in ['png', 'jpg', 'jpeg', 'tiff', 'bmp', 'gif', 'webp']
        if not check:
            return False      
    return True