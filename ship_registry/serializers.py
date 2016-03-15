from drf_hal_json import serializers as hal_serializers
from rest_framework import serializers

from .models import Company, Ship


class HalCollectionSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        items = super(HalCollectionSerializer, self).to_representation(data)
        return {
            '_links': {
                'self': '...',
            },
            '_embedded': {
                'item': items
            },
        }

    @property
    def data(self):
        pass


class RegistrySerializer(serializers.Serializer):
    hello = serializers.CharField()
    class Meta:
        list_serializer_class = HalCollectionSerializer


class CompanySerializer(hal_serializers.HalModelSerializer):
    class Meta:
        model = Company
        fields = ['name']
        list_serializer_class = HalCollectionSerializer


class ShipSerializer(hal_serializers.HalModelSerializer):
    class Meta:
        model = Ship
        fields = ['imo', 'name', 'owner']
        nested_fields = {
            'owner': (['name'], {}),
        }
        extra_kwargs = {
            'self': {
                'view_name': 'ship-detail',
                'lookup_field': 'imo',
            }
        }
        list_serializer_class = HalCollectionSerializer
