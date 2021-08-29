from django.urls import path
from mainapp.view.Delivery import DeliveryController

urlpatterns = [
    # ---------------- Url đăng nhập ----------------
    path('delivery/', DeliveryController.view_all_delivery_page, name='delivery'),
]