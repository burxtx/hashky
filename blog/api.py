#coding: UTF-8

from tastypie.resources import ModelResource
from blog.models import BlogPost

class BlogPostResource(ModelResource):
    class Meta:
        queryset = BlogPost.objects.all()
        resource_name = 'blogpost'
        

