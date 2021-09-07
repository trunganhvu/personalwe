from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def view_dashboard_page(request):
    """
    View dashboard page - need auth
    """
    return render(request, 'private/dashboard.html')