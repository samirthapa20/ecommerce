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
from addresses.views import checkout_address_create_view, checkout_address_reuse_view
from billing.views import payment_method_view, payment_method_createview
from accounts.views import LoginView, RegisterView, GuestRegisterView
from carts.views import cart_detail_api_view
from django.views.generic import TemplateView, RedirectView
from orders.views import LibraryView
# from marketing.views import MarketingPrefereceUpdateView
# from products.views import (
# 	ProductListView, 
# 	ProductDetailView,
# 	ProductFeaturedListView,
# 	ProductFeaturedDetailView,
# 	ProductDetailSlugView
# 	)
from django.urls import path, re_path
from django.contrib.auth import views as auth_views


urlpatterns = [
	url(r'^$', home_page, name="home"),
	url(r'^about/$', about_page, name="about"),
	# url(r'^accounts', RedirectView.as_view(url='/account')),
	url(r'^contact/$', contact_page, name="contact"),
	url(r'^account/', include(("accounts.urls","accounts"), namespace="account")),
	url(r'^accounts/', include(("accounts.passwords.urls","passwords"), namespace="password")),
	url(r'^orders/', include(("orders.urls","orders"), namespace="orders")),
	re_path(r'^password/change/done/$',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
	url(r'^login/$', LoginView.as_view(), name="login"),
	url(r'^checkout/address/create/$', checkout_address_create_view, name="checkout_address_create"),
	url(r'^checkout/address/reuse/$', checkout_address_reuse_view, name="checkout_address_reuse"),
	url(r'^register/guest/$', GuestRegisterView.as_view(), name="guest_register"),
	url(r'^library/$', LibraryView.as_view(), name="library"),
	url(r'^logout/$', LogoutView.as_view(), name="logout"),
	url(r'^api/cart/$', cart_detail_api_view, name="api-cart"),
	url(r'^cart/', include(("carts.urls","carts"), namespace="cart")),
	url(r'^billing/payment-method/$', payment_method_view, name="billing-payment-method"),
	url(r'^billing/payment-method/create/$', payment_method_createview, name="billing-payment-method-endpoint"),
	url(r'^register/$', RegisterView.as_view(), name="register"),
	url(r'^products/', include(("products.urls","products"), namespace="products")),
	url(r'^search/', include(("search.urls","search"), namespace="search")),
	# url(r'^settings/email/$', MarketingPrefereceUpdateView.as_view(), name='marketing-pref'),
	# url(r'^featured/$', ProductFeaturedListView.as_view()),
	# url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
	# # url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
	# url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
		urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
		urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)