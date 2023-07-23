from drf_spectacular.utils import extend_schema, extend_schema_view
from common.views.mixins import ListViewSet, LCRUDViewSet
from organizations.models.organizations import Organization, Employee
from organizations.serializers.api import employees as employees_s

@extend_schema_view(
    list=extend_schema(summary='Список сотрудников организации', tags=['Организации: Сотрудники']),
    retrieve=extend_schema(summary='Деталка сотрудника организации', tags=['Организации: Сотрудники']),
    create=extend_schema(summary='Создать сотрудника организации', tags=['Организации: Сотрудники']),
    update=extend_schema(summary='Изменить сотрудника организации', tags=['Организации: Сотрудники']),
    partial_update=extend_schema(summary='Изменить сотрудника организации частично', tags=['Организации: Сотрудники']),
    destroy=extend_schema(summary='Удалить сотрудника из организации', tags=['Организации: Сотрудники']),
    search=extend_schema(filters=True, summary='Список сотрудников организации Search', tags=['Словари']),
)


class EmployeeView(LCRUDViewSet):
    queryset = Employee.objects.all()
    serializer_class = employees_s.EmployeeCreateSerializer

    lookup_url_kwarg = 'employee_id'

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return employees_s.EmployeeRetrieveSerializer
        elif self.action == 'create':
            return employees_s.EmployeeCreateSerializer
        elif self.action == 'update':
            return employees_s.EmployeeUpdateSerializer
        elif self.action == 'partial_update':
            return employees_s.EmployeeUpdateSerializer
        return self.serializer_class

    def get_queryset(self):

        organization_id = self.request.parser_context['kwargs'].get('pk')

        queryset = Employee.objects.filter(
            organizations_id=organization_id
        )
        return queryset