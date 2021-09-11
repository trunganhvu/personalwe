from os import name
from django.urls import path
from mainapp.view.Delivery import DeliveryController
from mainapp.view.Home import HomeController
from mainapp.view.Header import HeaderConntroller, BannerTitleController
from mainapp.view.Home import DashboardController
from mainapp.view.Category import CategoryController
from mainapp.view.Category import CategoryPostController
from mainapp.view.User import UserController
from mainapp.view.ProductType import ProductTypeController
from mainapp.view.ProductType import ProductSizeController

urlpatterns = [
    # ---------------- Url manager ----------------
    path('delivery/', DeliveryController.view_all_delivery_page, name='delivery'),

    path('', HomeController.view_home_page, name='home'),
    path('home/', HomeController.view_home_page, name='home'),

    # ---------------- Url dashboard admin ----------------
    path('dashboard/', DashboardController.view_dashboard_page, name='dashboard'),

    # ---------------- Url header, title admin ----------------
    path('header/', HeaderConntroller.view_header_page, name='header'),
    path('header/image/', HeaderConntroller.insert_header_image_form, name='header-image'),
    path('banner-title/', BannerTitleController.update_banner_title_form, name='banner-title'),

    # ---------------- Url category admin ----------------
    path('category/', CategoryController.view_category_page, name='category'),
    path('category-form/', CategoryController.view_category_form_page, name='category-form'),
    path('category-form/insert/', CategoryController.insert_category_form, name='category-insert'),
    path('category/<int:id>/', CategoryController.get_category_detail_page, name='category-detail'),
    path('category-form/<str:id>/', CategoryController.view_category_form_update_page, name='category-form-update'),
    path('category-form/update/<str:id>', CategoryController.update_category_form, name='category-update'),

    # ---------------- Url post admin ----------------
    path('category/<str:category_id>/post-form/', CategoryPostController.view_insert_category_post_page, name='post-form'),
    path('category/<str:category_id>/post-form/<int:post_id>/', CategoryPostController.view_update_category_post_page, name='post-form-update'),
    path('category/<str:category_id>/post/<str:post_id>/', CategoryPostController.view_category_post_detail_page, name='post'),
    path('category/<str:category_id>/post-form/insert/', CategoryPostController.insert_category_post_form, name='post-insert'),
    path('category/<str:category_id>/post-form/<str:post_id>/update/', CategoryPostController.update_category_post_form, name='post-update'),
    path('post/<str:url>/', CategoryPostController.view_category_post_detail_public_page, name='public-post'),
    path('category/<str:url>/', CategoryController.view_category_by_url_public_page, name='public-category'),
    path('post/<int:post_id>/delete', CategoryPostController.delete_category_post_by_id, name='post-delete'),
    path('category/<int:category_id>/delete', CategoryController.delete_category_by_id, name='category-delete'),

    # ---------------- Url product type admin ---------------- 
    path('product-type/', ProductTypeController.get_all_product_type, name='product-type'),
    path('product-type/<int:product_type_id>/', ProductTypeController.view_product_type_detail_by_id, name='product-type-detail'),
    path('product-type-form/', ProductTypeController.view_product_type_insert_form_page, name='product-type-form'),
    path('product-type-form/<int:product_type_id>/', ProductTypeController.view_product_type_update_form_page, name='product-type-form-update'),
    path('product-type-form/insert/', ProductTypeController.insert_product_type, name='product-type-insert'),
    path('product-type-form/<int:product_type_id>/update', ProductTypeController.update_product_type, name='product-type-update'),
    path('product-type/<int:product_type_id>/delete', ProductTypeController.delete_product_type_by_id, name='product-type-delete'),

    # ---------------- Url product size admin ----------------
    path('product-type/<int:product_type_id>/product-size-form', ProductSizeController.view_product_size_insert_form_page, name='product-size-form'),
    path('product-type/<int:product_type_id>/product-size-form/insert/', ProductSizeController.insert_product_size, name='product-size-insert'),
    path('product-type/<int:product_type_id>/product-size/<int:product_size_id>/', ProductSizeController.view_product_size_detail_by_id, name='product-size-detail'),
    path('product-type/<int:product_type_id>/product-size-form/<int:product_size_id>/', ProductSizeController.view_product_size_update_form_page, name='product-size-form-update'),
    path('product-type/<int:product_type_id>/product-size/<int:product_size_id>/update/', ProductSizeController.update_product_size, name='product-size-update'),
    path('product-type/<int:product_type_id>/product-size/<int:product_size_id>/delete/', ProductSizeController.delete_product_size_by_id, name='product-size-delete'),


    # ---------------- Url login ----------------
    path('login/', UserController.view_login_page, name='login'),
    path('user-login/', UserController.user_login_form, name='user-login'),

    # ---------------- Url logout ----------------
    path('logout/', UserController.user_logout, name='logout'),

    
    # ---------------- API ----------------
    path('api/header/', HeaderConntroller.get_header_path, name='api-header'),
    path('api/banner-title/', BannerTitleController.get_banner_title, name='api-banner-title'),
]