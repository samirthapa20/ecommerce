"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from .views import home_page, about_page, contact_page
from accounts.views import login_page, register_page, guest_register_view

# from products.views import (
# 	ProductListView, 
# 	ProductDetailView,
# 	ProductFeaturedListView,
# 	ProductFeaturedDetailView,
# 	ProductDetailSlugView
# 	)


urlpatterns = [
	url(r'^$', home_page, name="home"),
	url(r'^about/$', about_page, name="about"),
	url(r'^contact/$', contact_page, name="contact"),
	url(r'^login/$', login_page, name="login"),
	url(r'^register/guest/$', login_page, name="guest_register_view"),
	url(r'^logout/$', LogoutView.as_view(), name="logout"),
	url(r'^cart/', include(("carts.urls","carts"), namespace="cart")),
	url(r'^register/$', register_page, name="register"),
	url(r'^products/', include(("products.urls","products"), namespace="products")),
	url(r'^search/', include(("search.urls","search"), namespace="search")),

	# url(r'^featured/$', ProductFeaturedListView.as_view()),
	# url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
	# # url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
	# url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
		urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
		urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)