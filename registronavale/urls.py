from django.conf.urls import include, url
from django.contrib import admin

from drf_hypermedia import routers
from . import views


admin.autodiscover()

urlpatterns = [
    url('^', include('ship_registry.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

router = routers.HypermediaRouter(trailing_slash=False)
router.register('', views.ApiRoot, 'api-root')
urlpatterns += router.urls
