from os import name
from django.urls import path
from mainapp.view.Delivery import DeliveryController
from mainapp.view.Home import HomeController
from mainapp.view.Header import HeaderConntroller, BannerTitleController
from mainapp.view.Home import DashboardController
from mainapp.view.Category import CategoryController, CategoryPostController
from mainapp.view.User import UserController
from mainapp.view.ProductType import ProductTypeController, ProductSizeController, ProductColorController
from mainapp.view.Event import EventController
from mainapp.view.Product import ProductController, ProductImageController, ProductPromotionController
from mainapp.view.ProductPublic import ProductController as PublicProductController
from mainapp.view.Cart import CartController

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

    # ---------------- Url product color admin ----------------
    path('product-type/<int:product_type_id>/product-color/<int:product_color_id>', ProductColorController.view_product_color_detail_by_id, name='product-color-detail'),
    path('product-type/<int:product_type_id>/product-color-form/', ProductColorController.view_product_color_insert_form_page, name='product-color-form'),
    path('product-type/<int:product_type_id>/product-color-form/<int:product_color_id>/', ProductColorController.view_product_color_update_form_page, name='product-color-form-update'),
    path('product-type/<int:product_type_id>/product-color-form/insert/', ProductColorController.insert_product_color, name='product-color-insert'),
    path('product-type/<int:product_type_id>/product-color-form/<int:product_color_id>/update/', ProductColorController.update_product_color, name='product-color-update'),
    path('product-type/<int:product_type_id>/product-color-form/<int:product_color_id>/delete/', ProductColorController.delete_product_color_by_id, name='product-color-delete'),

    # ---------------- Url product admin ----------------
    path('products/', ProductController.view_all_product_page, name='product'),
    path('products/<int:product_id>/', ProductController.view_product_detail_page, name='product-detail'),
    path('products/<int:product_id>/detail-form/', ProductController.view_update_product_detail_form_page, name='product-detail-form-update'),
    path('products/<int:product_id>/detail-form/update/<int:product_type_id>/', ProductController.update_product_and_product_detail, name='product-detail-update'),
    path('products/<int:product_type_id>/products-detail-form/', ProductController.view_insert_product_detail_form_page, name='product-detail-form-insert'),
    path('products/<int:product_type_id>/products-detail-form/insert/', ProductController.insert_product_and_product_detail, name='product-detail-insert'),
    path('products/<int:product_id>/images/', ProductController.view_modify_product_image_page, name='product-image-detail'),
    path('products/<int:product_id>/images/insert/', ProductImageController.insert_product_image_in_product, name='product-image-insert'),
    path('products/<int:product_id>/images/delete/', ProductImageController.delete_product_image_by_image_id, name='product-image-delete'),
    
    # ---------------- Url product promotion admin ----------------
    path('products/<int:product_id>/promotion/<int:product_promotion_id>/', ProductPromotionController.view_detail_product_promotion_by_promotion_id, name='product-promotion-detail'),
    path('products/<int:product_id>/promotion-form/', ProductPromotionController.view_product_promotion_form_insert_page, name='product-promotion-form-insert'),
    path('products/<int:product_id>/promotion-form/<int:product_promotion_id>', ProductPromotionController.view_product_promotion_form_update_page, name='product-promotion-form-update'),
    path('products/<int:product_id>/promotion-form-insert/', ProductPromotionController.insert_product_promotion, name='product-promotion-insert'),
    path('products/<int:product_id>/promotion-form/<int:product_promotion_id>/update/', ProductPromotionController.update_product_promotion, name='product-promotion-update'),
    path('products/<int:product_id>/promotion/<int:product_promotion_id>/delete/', ProductPromotionController.delete_product_promotion_by_promotion_id, name='product-promotion-delete'),

    # ---------------- Url shop public ----------------
    path('shop/', PublicProductController.get_all_product, name='public-list-product'),
    path('shop/type<int:product_type_id>/', PublicProductController.get_all_product_in_product_type_id, name='public-list-product-type'),
    path('shop/product/<int:product_id>/', PublicProductController.get_product_detail_by_product_id, name='public-product-detail'),

    # ---------------- Url event admin ----------------
    path('event/', EventController.view_all_event, name='event'),
    path('event-form/', EventController.view_event_insert_form_page, name='event-form'),
    path('event/<int:event_id>/', EventController.view_event_detail_by_id, name='event-detail'),
    path('event/insert/', EventController.insert_event, name='event-insert'),
    path('event-form/<int:event_id>/', EventController.view_event_update_form_page, name='event-form-update'),
    path('event-form/<int:event_id>/update/', EventController.update_event, name='event-update'),
    path('event-form/<int:event_id>/delete/', EventController.delete_event_by_id, name='event-delete'),


    # ---------------- Url login ----------------
    path('login/', UserController.view_login_page, name='login'),
    path('user-login/', UserController.user_login_form, name='user-login'),

    # ---------------- Url logout ----------------
    path('logout/', UserController.user_logout, name='logout'),

    
    # ---------------- API ----------------
    path('api/header/', HeaderConntroller.get_header_path, name='api-header'),
    path('api/banner-title/', BannerTitleController.get_banner_title, name='api-banner-title'),


    path('api/cart/<str:key>/', CartController.count_item_in_cart_by_key, name='api-cart-count'),
]