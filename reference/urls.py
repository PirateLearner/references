'''
Created on 31-Jul-2015

@author: anshul
'''
from django.conf.urls import patterns, include, url

from reference.views import ReferenceDetail, ReferenceList

urlpatterns = patterns('',
    url(r'^reference/(?P<article>\d+)/$', ReferenceList.as_view(), name='reference_list'),
    url(r'^reference/(?P<article>\d+)/(?P<ref>\d+)/$', ReferenceDetail.as_view(), name="reference_detail"),
    )