from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.api_root, name='api-root'),
    url(r'^company/(?P<pk>[0-9]+)$', views.CompanyDetail.as_view(), name='company-detail'),
    url(r'^ships$', views.search_ships, name='ship-search'),
    url(r'^ship/(?P<imo>[0-9]+)$', views.ShipDetail.as_view(), name='ship-detail'),
]
