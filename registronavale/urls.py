from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url('^', include('ship_registry.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
