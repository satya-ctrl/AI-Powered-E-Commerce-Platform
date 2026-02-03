from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("product/<int:id>/", product_detail, name="product_detail"),
    path("add/<int:id>/", add_to_cart, name="add_to_cart"),
    path("cart/", cart, name="cart"),
    path("checkout/", checkout, name="checkout"),
    path("login/", user_login, name="login"),
    path("register/", register, name="register"),
    path("chatbot/", chatbot, name="chatbot"),
]
