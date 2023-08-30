from django.urls import path, include
from rest_framework.routers import DefaultRouter

from organizations.views import dicts, organizations, employees, groups, offers

router = DefaultRouter()

router.register(r'dicts/positions', dicts.PositionView, 'positions')
router.register(r'search', organizations.OrganizationSeachView, 'organizations-search')
router.register(r'(?P<pk>\d+)/employees', employees.EmployeeView, 'employees')
router.register(r'offers', offers.OfferUserView, 'user-offers')
router.register(r'(?P<pk>\d+)/offers', offers.OfferOrganisationView, 'org-offers')
router.register(r'groups', groups.GroupView, 'groups')
router.register(r'', organizations.OrganizationView, 'organizations')

urlpatterns = [
    path('organizations/', include(router.urls)),
]