from django.conf.urls import url
from . import  views

urlpatterns = [
    url(r'^index/$',views.index, name='index'),
    url(r'^detail/$',views.goods_detail, name='detail'),
    url(r'^list/(\d+)/(\d+)/$',views.goods_list,name='list'),

]