from django.conf.urls import patterns, include, url
from django.contrib import admin
from testapp.api import PersonResource

admin.autodiscover()

person_resource = PersonResource()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'testapp.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       (r'^api/', include(person_resource.urls))
                       )
