from django.shortcuts import render
from mainapp.service.Category import CategoryService

def view_home_page(request):
    """
    View home page
    """
    list_category = CategoryService.get_category_display()
    context = {
        'categories': list_category
    }
    return render(request, 'public/Home/home.html', context=context)