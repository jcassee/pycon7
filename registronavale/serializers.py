from rest_framework import serializers

from drf_hypermedia import reverse
from drf_hypermedia.serializers import HalSerializer
from registronavale import profiles
from registronavale import relations


class ApiRootSerializer(HalSerializer):
    class Meta:
        view_name = 'api-root'


    version = serializers.CharField()

    @classmethod
    def get_links(cls, request, instance=None):
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
