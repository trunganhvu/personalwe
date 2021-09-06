from django.shortcuts import render
from mainapp.service.Category import CategoryService
from mainapp.service.Category import CategoryPostService
from mainapp.Common import ConstValiable
def view_home_page(request):
    """
    View home page
    """
    list_category = CategoryService.get_category_display()
    categories = []
    for category_item in list_category:
        list_post = {}
        display_type = category_item.display_type
        if display_type == ConstValiable.CATEGORY_DISPLAY_TYPE_1:
            number_post = ConstValiable.LIMIT_POST_IN_HOME_TYPE_1
        elif display_type == ConstValiable.CATEGORY_DISPLAY_TYPE_2:
            number_post == ConstValiable.LIMIT_POST_IN_HOME_TYPE_2
        else:
            number_post == ConstValiable.LIMIT_POST_IN_HOME_TYPE_3
            
        list_category_post = CategoryPostService.get_limit_post_display_in_category(category_item.category_id, number_post)

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