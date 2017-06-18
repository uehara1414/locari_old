from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mypage/$', views.mypage, name='mypage'),
    url(r'^search/$', views.search, name='search'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^wish/$', views.wish, name='wish'),
    url(r'^onsale/$', views.onsale, name='onsale'),
    url(r'^confirming/$', views.confirming, name='confirming'),
    url(r'^sale_request/$', views.sale_request, name='sale_request'),
]
