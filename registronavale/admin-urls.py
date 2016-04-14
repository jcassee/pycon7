from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/admin/', permanent=True), name='index'),
    url(r'^admin/', include(admin.site.urls)),
]
