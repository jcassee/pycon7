from rest_framework.serializers import ModelSerializer

from drf_hal.serializers import HalCollectionSerializer, HalSerializer
from registronavale import profiles, relations, deprecations
from .models import Company, Ship, ShipOwnership


class CompanySerializer(HalSerializer, ModelSerializer):
    class Meta:
        model = Company
        fields = ['name']
        list_serializer_class = HalCollectionSerializer
        profile = profiles.COMPANY
        view_name = 'company'

    def get_links(self, request, instance=None):
        return {
            relations.OWNED_SHIPS: self.link('company-ships', kwargs={'pk': instance.pk}, deprecation=deprecations.SHIP_OWNER),
            relations.OWNER_HISTORY: self.link('company-ships-history', kwargs={'pk': instance.pk}),
        }


class ShipSerializer(HalSerializer, ModelSerializer):
    class Meta:
        model = Ship
        fields = ['imo', 'name']
        list_serializer_class = HalCollectionSerializer
        profile = profiles.SHIP
        view_name = 'ship'
        lookup_field = 'imo'

    def get_links(self, request, instance=None):
        ret = {
            relations.OWNER_HISTORY: self.link('ship-owners-history', kwargs={'imo': instance.imo}),
        }
        if instance.owner is not None:
            ret[relations.SHIP_OWNER] = self.link('company', kwargs={'pk': instance.owner.pk}, deprecation=deprecations.SHIP_OWNER)
        return ret


class ShipOwnershipSerializer(HalSerializer, ModelSerializer):
    class Meta:
        model = ShipOwnership
        fields = ['begin', 'end']
        list_serializer_class = HalCollectionSerializer
        profile = profiles.SHIP_OWNERSHIP
        view_name = 'ship-ownership'

    def get_embedded(self, request, instance=None):
        return {
            relations.SHIP_OWNER: CompanySerializer(instance.company, include_embedded=False, context=self.context).data,
            relations.OWNED_SHIP: ShipSerializer(instance.ship, include_embedded=False, context=self.context).data,
        }
