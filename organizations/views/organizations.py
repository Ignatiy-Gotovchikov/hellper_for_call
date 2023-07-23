from django.db.models import Count, Case, When
from django_filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.filters import SearchFilter

from common.views.mixins import ListViewSet, LCRUViewSet
from organizations.backends import MyOrganisation
from organizations.models.organizations import Organization
from organizations.permissions import IsMyOrganization
from organizations.serializers.api import organizations

@extend_schema_view(
    list=extend_schema(summary='Список организаций Search', tags=['Словари']),
)

class OrganizationSeachView(ListViewSet):
    queryset = Organization.objects.all()
    serializer_class = organizations.OrganizationSearchListSerializer


@extend_schema_view(
    list=extend_schema(summary='Список организаций', tags=['Организации']),
    retrieve=extend_schema(summary='Деталка организации', tags=['Организации']),
    create=extend_schema(summary='Создать организацию', tags=['Организации']),
    update=extend_schema(summary='Изменить организацию', tags=['Организации']),
    partial_update=extend_schema(summary='Изменить организацию частично', tags=['Организации']),
)
class OrganizationView(LCRUViewSet):
    permission_classes = [IsMyOrganization]
    queryset = Organization.objects.all()
    serializer_class = organizations.OrganizationListSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return organizations.OrganizationRetrieveSerializer
        elif self.action == 'create':
            return organizations.OrganizationCreateSerializer
        elif self.action == 'update':
            return organizations.OrganizationUpdateSerializer
        elif self.action == 'partial_update':
            return organizations.OrganizationUpdateSerializer

        return self.serializer_class


class OrganisationView(LCRUViewSet):
    permission_classes = [IsMyOrganization]
    queryset = Organization.objects.all()
    serializer_class = organizations.OrganizationListSerializer

    multi_serializer_class = {
        'list': organizations.OrganizationListSerializer,
        'retrieve': organizations.OrganizationRetrieveSerializer,
        'create': organizations.OrganizationCreateSerializer,
        'update': organizations.OrganizationUpdateSerializer,
        'partial_update': organizations.OrganizationUpdateSerializer,
    }

    http_method_names = ('get', 'post', 'patch')

    filter_backends = (
        OrderingFilter,
        SearchFilter,
        DjangoFilterBackend,
        MyOrganisation,
    )
    # filterset_class = OrganizationFilter
    ordering = ('name', 'id',)

    def get_queryset(self):
        queryset = Organization.objects.select_related(
            'director',
        ).prefetch_related(
            'employees',
            'groups',
        ).annotate(
            pax=Count('employees', distinct=True),
            groups_count=Count('groups', distinct=True),
            can_manage=Case(
                When(director=self.request.user, then=True),
                default=False,
            )
        )
        return queryset






