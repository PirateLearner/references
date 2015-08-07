'''
Created on 31-Jul-2015

@author: anshul
'''
from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns

from reference.views import (ReferenceDetail, ReferenceList,
                             BlogContentViewSet, UserViewSet,
                             CurrentUserView,  BlogContentRefView,
                             api_root
                            )
                             
blogcontent_list = BlogContentViewSet.as_view({
    'get': 'list'                                           
    })
blogcontent_detail = BlogContentViewSet.as_view({
    'get': 'retrieve',
    })

user_list = UserViewSet.as_view({
    'get': 'list'
    })
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
    })

urlpatterns = patterns('',
    url(r'^blogcontent/$', blogcontent_list, name='blogcontent-list'),
    url(r'^blogcontent/(?P<pk>[0-9]+)/$', blogcontent_detail, name='blogcontent-detail'),
    url(r'^blogcontent/(?P<pk>[0-9]+)/reference/$', BlogContentRefView.as_view(), name='blogcontent-references'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/current/$', CurrentUserView.as_view(), name='current-user'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
    url(r'^rest/$', api_root),
    url(r'^reference/$', ReferenceList.as_view(), name='reference_list'),
    url(r'^reference/(?P<article>\d+)/(?P<ref>\d+)/$', ReferenceDetail.as_view(), name="reference_detail"),
    )
urlpatterns += patterns('',
    url(r'^cr/(\d+)/(.+)/$', 'django.contrib.contenttypes.views.shortcut', name='comments-url-redirect'),
)
urlpatters = format_suffix_patterns(urlpatterns)