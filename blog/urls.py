from django.conf.urls import url
from django.contrib import admin
from blog.views import post_detail, PostList, PostCreate, PostUpdate, PostDelete

urlpatterns = [
	url(r'^$', PostList.as_view(), name='blog_list'),

	url(r'^create/$', PostCreate.as_view(), name='blog_create_post'),
	url(r'^(?P<year>\d{4})/'
		r'(?P<month>\d{1,2})/'
		r'(?P<slug>[\w\-]+)/$', post_detail, name='blog_post_detail'),
	url(r'^(?P<year>\d{4})/'
		r'(?P<month>\d{1,2})/'
		r'(?P<slug>[\w\-]+)/'
		r'update/$', PostUpdate.as_view(), name='blog_post_update'),
	url(r'^(?P<year>\d{4})/'
		r'(?P<month>\d{1,2})/'
		r'(?P<slug>[\w\-]+)/'
		r'delete/$', PostDelete.as_view(), name='blog_post_delete'),
]
