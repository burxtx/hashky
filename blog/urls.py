# from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import FormView
from blog.forms import BlogPostSaveForm
from blog.api import BlogPostResource
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
blogpost_resource = BlogPostResource()
urlpatterns = patterns('blog.views',
    (r'^$', 'main_page'),
    url(r'^user/(\w+)/$', 'user_page', name="user_page"),
    url(r'^user/(\w+)/draft/$', 'draft_page', name="draft_page"),
    (r'^tag/([^\s]+)/$', 'tag_page'),
    # (r'^tag/$', tag_cloud_page),
    (r'^search/$', 'search_page'),
    url(r'^blogpost/(\d+)/$', 'blogpost_detail_page', name="blogpost_detail"),
    url(r'^draft/(\d+)/$', 'draft_detail_page', name="draft_detail"),
    # (r'^site_media/(?P<path>.*)$', 'django.views.static.server',
    #     { 'document_root':site_media }),
    # (r'^site_media/css/(?P<path>.*)$', 'django.views.static.server',
    #     { 'document_root':site_media + '/css/' }),
    # (r'^site_media/js/(?P<path>.*)$', 'django.views.static.server',
    #     { 'document_root':site_media + '/js/' }),
    # (r'^site_media/img/(?P<path>.*)$', 'django.views.static.server',
    #     { 'document_root':site_media + '/img/' }),
    url(r'^save/$', 'blogpost_save_page', name="blogpost_save"),
    url(r'^blogpost/edit/(\d+)/$', 'blogpost_save_page', name="blogpost_update"),
    url(r'^blogpost/delete/(\d+)/$', 'blogpost_delete', name="blogpost_delete"),
    # Friends
    (r'^following/(\w+)/$', 'friends_page'),
    (r'^friend/add/$', 'friend_add'),
    (r'^friend/remove/$', 'friend_remove'),
    (r'^ajax/tag/autocomplete/$', 'ajax_tag_autocomplete'),
    url(r'^$', FormView.as_view(
        template_name="blogpost_detail.html",
        form_class=BlogPostSaveForm)),
)

# urlpatterns = [
#     # ... the rest of your URLconf goes here ...
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG :
#     urlpatterns += patterns('',
#         (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
#     )