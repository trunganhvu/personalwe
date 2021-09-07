import re
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.models import User
from mainapp.service.User import UserService
from mainapp.Common import ConstValiable

def view_login_page(request):
    """
    View login page
    """
    if request.user.is_authenticated:
        return redirect('/dashboard')
    else:
        return render(request, 'private/User/login.html')

def user_login_form(request):
    """
    Authentication user
    """
    if request.user.is_authenticated:
        return redirect('/dashboard')
    else:
        if request.method == 'POST':
            try:
                username = request.POST.get('username')
                password = request.POST.get('password')
                context = {
                    'username': username
                }
                next = request.GET.get('next')
                msg = UserService.user_login(request, username, password)
                if msg == '':
                    if next != '':
                        return redirect(next)
                    return redirect('/dashboard')
                else:
                    messages.error(request, msg)
                    return render(request, 'private/User/login.html', context=context)

            except Exception:
                messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
                return render(request, 'private/User/login.html')

def user_logout(request):
    """
    User logout
    """
    logout(request)
    return redirect('/')