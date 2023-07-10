from drf_spectacular.utils import extend_schema, extend_schema_view
from common.views.mixins import DictListMixin
from organizations.models.dicts import Position


@extend_schema_view(
    list=extend_schema(summary='Список должностей', tags=['Словари']),
)

class PositionView(DictListMixin):
    queryset = Position.objects.filter(is_active=True)
