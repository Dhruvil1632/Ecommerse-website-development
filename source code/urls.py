from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index , name = "homeshop"),
    path('home.html',views.index , name = "homeshop"),
    path('signup.html',views.return_sign , name = "signup"),
    path('signup',views.signup , name = "signup"),
    path('contact.html',views.contact , name = "contact"),
    path('login.html',views.return_login , name = "return_login"),
    path('login',views.login , name = "login"),
    path('mycart.html' , views.cart , name = 'cart'),
    path('add_to_cart' , views.add_to_cart, name = 'my_cart'),
    path('add_to_cart1' , views.add_to_cart1, name = 'my_cart'),
    path('remove_from_cart' , views.remove_product, name = 'rem_product'),
    path('search_in_cart' , views.search_in_cart , name = 'search_cart'),
    path('return_page' , views.index , name = 'return_home'),
    path('search',views.search, name = "login"),
    path('slider' , views.slider , name = 'slider'),
    path('payment' , views.payment , name = 'payment'),
    path('purchase' , views.purchase , name = 'purchase')
    ]

