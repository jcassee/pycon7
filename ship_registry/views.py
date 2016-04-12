from rest_framework.generics import get_object_or_404
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response

from drf_hypermedia import reverse
from drf_hypermedia.views import HypermediaViewSet, HypermediaRetrieveModelMixin
from registronavale import relations
from . import models
from . import serializers


class SearchShips(ListModelMixin, HypermediaViewSet):
    serializer_class = serializers.ShipSerializer

    def get_queryset(self):
        query = self.request.query_params['q']
        return models.Ship.objects.filter(name__contains=query)

    def retrieve(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class Company(HypermediaRetrieveModelMixin, HypermediaViewSet):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer

    def get_links(self, instance, request):
        return {
            relations.OWNED_SHIPS: {
                'href': reverse(CompanyShips, kwargs={'pk': instance.pk}, request=request)
            },
        }


class CompanyShips(ListModelMixin, HypermediaViewSet):
    serializer_class = serializers.ShipSerializer

    def get_queryset(self):
        queryset = models.Company.objects.prefetch_related('ships')
        company = get_object_or_404(queryset, pk=self.kwargs['pk'])
        return company.ships.all()

    def retrieve_model(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class Ship(HypermediaRetrieveModelMixin, HypermediaViewSet):
    lookup_field = 'imo'
    serializer_class = serializers.ShipSerializer

    def get_queryset(self):
        return models.Ship.objects.filter(imo=self.kwargs['imo'])

    def get_links(self, instance, request):
        return {
            relations.SHIP_OWNER: {
                'href': reverse(Company, kwargs={'pk': instance.owner.pk}, request=request),
            },
        }
