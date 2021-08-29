from django.shortcuts import render

def view_all_delivery_page(request):
    return render(request, 'public/Delivery/delivery.html')
