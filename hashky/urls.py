from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from blog.api import BlogPostResource
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
blogpost_resource = BlogPostResource()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hashky.views.home', name='home'),
    # url(r'^hashky/', include('hashky.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^ratings/', include('ratings.urls')),
    (r'^api/', include(blogpost_resource.urls)),
    url(r'^', include('blog.urls', namespace="blog")),
    url(r'^wechat/',include('wechat.urls', namespace="wechat")),
    url(r'^', include('account.urls', namespace="account")),
)
# urlpatterns = [
#     # ... the rest of your URLconf goes here ...
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)