from rest_framework.generics import get_object_or_404
from rest_framework.mixins import ListModelMixin
from rest_framework.reverse import reverse
from rest_framework.viewsets import GenericViewSet

from drf_hal.views import HalRetrieveModelMixin
from registronavale import relations
from . import models
from . import serializers


class SearchShips(ListModelMixin, GenericViewSet):
    serializer_class = serializers.ShipSerializer

    def get_queryset(self):
        query = self.request.query_params['q']
        return models.Ship.objects.filter(name__contains=query)

    def retrieve(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class Company(HalRetrieveModelMixin, GenericViewSet):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer


class CompanyShips(ListModelMixin, GenericViewSet):
    serializer_class = serializers.ShipSerializer

    def get_queryset(self):
        queryset = models.Company.objects.prefetch_related('ships')
        company = get_object_or_404(queryset, pk=self.kwargs['pk'])
        return company.ships.all()

    def retrieve_model(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class Ship(HalRetrieveModelMixin, GenericViewSet):
    queryset = models.Ship.objects.all()
    lookup_field = 'imo'
    serializer_class = serializers.ShipSerializer
