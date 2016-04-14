from drf_hal import routers
from . import views

router = routers.HypermediaRouter(trailing_slash=False)
router.register('search', views.SearchShips, 'search-ships')
router.register('company', views.Company, 'company')
router.register('company-ships', views.CompanyShips, 'company-ships')
router.register('ship', views.Ship, 'ship')
router.register('ship-ownership', views.ShipOwnership, 'ship-ownership')
router.register('company-ships-history', views.CompanyOwnershipHistory, 'company-ships-history')
router.register('ship-owners-history', views.ShipOwnershipHistory, 'ship-owners-history')
urlpatterns = router.urls
