
from django.urls import path
from .import views


urlpatterns = [
    path("", views.index,name="index"),
    path("home/", views.home,name="home"),
    path("shop-single/", views.shopSingle,name="shop-single"),
    path("shop/", views.shop,name="shop"),
]

#manoranjan/justtoy@1