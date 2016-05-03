"""drf_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from products.views import ManufacturerViewSet, CategoryViewSet, ProductViewSet, ProductImageViewSet
from accounts.views import UserSignupView, UserViewSet
from carts.views import add_to_cart
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'manufacturers', ManufacturerViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'productimages', ProductImageViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/signup', UserSignupView.as_view(), name='user_signup'),
    url(r'^api/v1/addtocart', add_to_cart, name='add_to_cart'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
