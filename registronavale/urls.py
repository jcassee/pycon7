from django.conf.urls import include, url
from django.contrib import admin

from . import views


admin.autodiscover()

urlpatterns = [
    url(r'^$', views.api_root, name='api-root'),
    url('^', include('ship_registry.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
