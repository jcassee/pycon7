from rest_framework import serializers
from rest_framework.reverse import reverse

from drf_hal.serializers import HalSerializer
from registronavale import relations


class ApiRootSerializer(HalSerializer):
    version = serializers.CharField()

    class Meta:
        view_name = 'api-root'

    def get_links(self, request, instance=None):
        return {
            relations.SHIP_BY_IMO: {
                'href': reverse('ship', kwargs={'imo': 'IMO'}, request=request).replace('IMO', '{imo}'),
                'templated': True,
            },
            relations.SEARCH_SHIPS: {
                'href': reverse('search-ships', request=request) + '{?q}',
                'templated': True,
            },
        }
