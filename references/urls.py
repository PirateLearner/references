from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'references.views.home', name='home'),
    url(r'^reference/','reference.urls', name='referece'),
    url(r'^contact/$', 'voting_demo.views.contact', name='contact'),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^blogging/', include('blogging.urls',namespace='blogging')),
    url(r'^select2/', include('django_select2.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
