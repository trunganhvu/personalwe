from django.shortcuts import render
from mainapp.service.Category import CategoryService
from mainapp.service.Category import CategoryPostService

def view_home_page(request):
    """
    View home page
    """
    list_category = CategoryService.get_category_display()
    categories = []
    for category_item in list_category:
        list_post = {}

        list_category_post = CategoryPostService.get_limit_post_display_in_category(category_item.category_id)

        if len(list_category_post) > 0:
            list_post = list_category_post
        category = {
            'category_detail': category_item,
            'posts': list_post
        }
        categories.append(category)
    context = {
        'categories': categories,
    }
    return render(request, 'public/Home/home.html', context=context)