from drf_hypermedia import routers
from . import views

router = routers.HypermediaRouter(trailing_slash=False)
router.register('search', views.SearchShips, 'search-ships')
router.register('company', views.Company, 'company')
router.register('company-ships', views.CompanyShips, 'company-ships')
router.register('ship', views.Ship, 'ship')
urlpatterns = router.urls
