from django.contrib.auth import login, logout, get_user_model, authenticate
from django.contrib.auth.models import User
import re

def user_login(request, username, password):
    """
    Check auth account and update time login
    """
    msg = ''
    if username.strip() == "" or password.strip() == "":
        msg = 'Hãy nhập đầy đủ thông tin.'
    elif not re.match('[A-Za-z0-9_-]{6,30}$', username):
        msg = 'Hãy nhập Tên đăng nhập đúng định dạng.'
    
    if msg == '':
        # users = get_user_model()
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
        else:
            msg = 'Tên đăng nhập hoặc mật khẩu sai.'

    return msg
