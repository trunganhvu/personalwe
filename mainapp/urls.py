from django.urls import path
from mainapp.view.Delivery import DeliveryController
from mainapp.view.Home import HomeController
from mainapp.view.Header import HeaderConntroller

urlpatterns = [
    # ---------------- Url đăng nhập ----------------
    path('delivery/', DeliveryController.view_all_delivery_page, name='delivery'),

    path('', HomeController.view_home_page, name='home'),
    path('home/', HomeController.view_home_page, name='home'),



    # ---------------- API ----------------
    path('api/header/', HeaderConntroller.get_header_path, name='api-header'),

]