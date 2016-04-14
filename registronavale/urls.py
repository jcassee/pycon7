from django.conf.urls import include, url

from drf_hal import routers
from . import views


urlpatterns = [
    url('^', include('ship_registry.urls')),
]

router = routers.HypermediaRouter(trailing_slash=False)
router.register('', views.ApiRoot, 'api-root')
urlpatterns += router.urls
