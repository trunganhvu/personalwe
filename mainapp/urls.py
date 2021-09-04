from os import name
from django.urls import path
from mainapp.view.Delivery import DeliveryController
from mainapp.view.Home import HomeController
from mainapp.view.Header import HeaderConntroller, BannerTitleController
from mainapp.view.Home import DashboardController
from mainapp.view.Category import CategoryController
from mainapp.view.Category import CategoryPostController

urlpatterns = [
    # ---------------- Url đăng nhập ----------------
    path('delivery/', DeliveryController.view_all_delivery_page, name='delivery'),

    path('', HomeController.view_home_page, name='home'),
    path('home/', HomeController.view_home_page, name='home'),
    path('dashboard/', DashboardController.view_dashboard_page, name='dashboard'),
    path('header/', HeaderConntroller.view_header_page, name='header'),
    path('header/image/', HeaderConntroller.insert_header_image_form, name='header-image'),
    path('banner-title/', BannerTitleController.update_banner_title_form, name='banner-title'),
    path('category/', CategoryController.view_category_page, name='category'),
    path('category-form/', CategoryController.view_category_form_page, name='category-form'),
    path('category-form/insert/', CategoryController.insert_category_form, name='category-insert'),
    path('category/<str:id>/', CategoryController.get_category_detail_page, name='category-detail'),
    path('category-form/<str:id>/', CategoryController.view_category_form_update_page, name='category-form-update'),
    path('category-form/update/<str:id>', CategoryController.update_category_form, name='category-update'),
    path('category/<str:category_id>/post-form/', CategoryPostController.view_insert_category_post_page, name='post-form'),
    path('category/<str:category_id>/post-form/<int:post_id>/', CategoryPostController.view_update_category_post_page, name='post-form-update'),
    path('category/<str:category_id>/post/<str:post_id>/', CategoryPostController.view_category_post_detail_page, name='post'),
    path('category/<str:category_id>/post-form/insert/', CategoryPostController.insert_category_post_form, name='post-insert'),
    path('category/<str:category_id>/post-form/<str:post_id>/update/', CategoryPostController.update_category_post_form, name='post-update'),




    # ---------------- API ----------------
    path('api/header/', HeaderConntroller.get_header_path, name='api-header'),
    path('api/banner-title/', BannerTitleController.get_banner_title, name='api-banner-title'),
]