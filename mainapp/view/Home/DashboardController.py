from django.shortcuts import render

def view_dashboard_page(request):
    return render(request, 'private/dashboard.html')