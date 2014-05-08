from django.conf.urls import patterns, include, url

urlpatterns=patterns('wechat.views',
    url(r'^$','index'),
    # url(r'^product//$','wechat.views.product_list'),
    url(r'^product/(\d+)/$','product_detail'),
    url(r'^binding/$', 'bind_wechat'),
    url(r'^product/(\w+)/$', 'product_page'),
    url(r'^product/$', 'product_main_page')
)

