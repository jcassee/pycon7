from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^company/(?P<pk>.+)$', views.CompanyDetail.as_view(), name='company-detail'),
    url(r'^ships$', views.search_ships, name='ship-search'),
    url(r'^ship/(?P<imo>.+)$', views.ShipDetail.as_view(), name='ship-detail'),
]
