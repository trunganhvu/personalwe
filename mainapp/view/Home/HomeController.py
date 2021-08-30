from django.shortcuts import render

def view_home_page(request):
    return render(request, 'public/Home/home.html')