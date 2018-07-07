from django.conf.urls import patterns, url

from webshop.views import MyShopListView, MyProductDetailView, KatView, DoubleKatView, KatView2
#from shop.views.product import ProductDetailView
from shop.models.productmodel import Product


urlpatterns = patterns('',
    url(r'^$',
        MyShopListView.as_view(model=Product),
        name='product_list'
        ),
    url(r'^kategorie/([\w-]+)/([\w-]+)/$', DoubleKatView.as_view(model=Product)),
    url(r'^kategorie/([\w-]+)/$', KatView2.as_view()),
    #url(r'^kategorie/([\w-]+)/$', KatView.as_view(model=Product)),
    url(r'^(?P<slug>[0-9A-Za-z-_.//]+)/$',
        MyProductDetailView.as_view(),
        name='product_detail'
        ),
   
    )
