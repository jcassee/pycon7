from rest_framework.serializers import ModelSerializer, reverse

from drf_hypermedia.serializers import HalCollectionSerializer, HalSerializer
from registronavale import profiles, relations

from .models import Company, Ship


class CompanySerializer(HalSerializer, ModelSerializer):
    class Meta:
        model = Company
        fields = ['name']
        list_serializer_class = HalCollectionSerializer
        profile = profiles.COMPANY
        view_name = 'company'

    def get_links(self, request, instance=None):
        return {
            relations.OWNED_SHIPS: {
                'href': reverse('company-ships', kwargs={'pk': instance.pk}, request=request)
            },
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
        ret = {}
        if instance.owner is not None:
            ret[relations.SHIP_OWNER] = {'href': reverse('company', kwargs={'pk': instance.owner.pk}, request=request)}
        return ret

    def get_embedded(self, request, instance=None):
        ret = {}
        if instance.owner is not None:
            ret[relations.SHIP_OWNER] = CompanySerializer(instance.owner, include_embedded=False, context=self.context).data
        return ret
