from django.urls import path
from django.conf.urls import url
from .views import AccountHomeView,UserDetailUpdateView
from products.views import UserProductHistoryView
urlpatterns = [
	url(r'^$', AccountHomeView.as_view(), name='home'),
	url(r'^details/$', UserDetailUpdateView.as_view(), name='user-update'),
	url(r'history/products/$', UserProductHistoryView.as_view(), name='user-product-history'),
]

