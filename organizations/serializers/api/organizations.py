from crum import get_current_user
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ParseError

from common.serializers.mixins import ExtendedModelSerializer
from organizations.models.organizations import Organization
from users.serializers.nested.users import UserShortSerializer


User = get_user_model()


class OrganizationSearchListSerializer(ExtendedModelSerializer):
    director = UserShortSerializer()

    class Meta:
        model = Organization
        fields = (
            'id',
            'name',
            'director',
        )


class OrganizationListSerializer(ExtendedModelSerializer):
    director = UserShortSerializer()

    class Meta:
        model = Organization

        fields = (
            'id',
            'name',
            'director',
        )


class OrganizationRetrieveSerializer(ExtendedModelSerializer):
    director = UserShortSerializer()

    class Meta:
        model = Organization

        fields = (
            'id',
            'name',
            'director',
        )


class OrganizationCreateSerializer(ExtendedModelSerializer):
    class Meta:
        model = Organization
        fields = (
            'id',
            'name',
        )


class OrganizationUpdateSerializer(ExtendedModelSerializer):
    class Meta:
        model = Organization
        fields = (
            'id',
            'name',
        )


