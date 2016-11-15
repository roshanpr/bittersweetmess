from django.conf.urls import url
from django.contrib import admin
from organizer.views import tag_detail, tag_list, startup_detail, tag_create, TagCreate, StartupCreate, NewsLinkCreate, NewsLinkUpdate, StartupUpdate, TagUpdate, NewsLinkDelete, StartupList

urlpatterns = [
	url(r'^tag/$', tag_list, name='organizer_tag_list'),
	# url(r'^tag/create/$', tag_create, name='organizer_create_tag'),
	url(r'^tag/create/$', TagCreate.as_view(), name='organizer_create_tag'),
	url(r'^tag/(?P<slug>[\w\-]+)/update/$', TagUpdate.as_view(), name='organizer_update_tag'),
	url(r'^startup/create/$', StartupCreate.as_view(), name='organizer_create_startup'),
	url(r'^newslink/create/$', NewsLinkCreate.as_view(), name='organizer_create_newslink'),
	url(r'^newslink/update/(?P<pk>\d+)/$', NewsLinkUpdate.as_view(), name='organizer_update_newslink'),
	url(r'^newslink/delete/(?P<pk>\d+)/$', NewsLinkDelete.as_view(), name='organizer_delete_newslink'),
	# url(r'^tag/create/$', create_tag, name='organizer_create_tag'),

	url(r'^startup/$', StartupList.as_view(), name='organizer_startup_list'), 
	url(r'^tag/(?P<slug>[\w\-]+)/$', tag_detail, name='organizer_tag_detail'),
	url(r'^startup/(?P<slug>[\w\-]+)/$', startup_detail, name='organizer_start_up_detail'),
	url(r'^startup/(?P<slug>[\w\-]+)/update/$', StartupUpdate.as_view(), name='organizer_start_up_update'),
	
]
