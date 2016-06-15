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
        return models.Ship.objects.filter(name__icontains=query)

    def retrieve(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class Company(HalRetrieveModelMixin, GenericViewSet):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer


class CompanyShips(ListModelMixin, GenericViewSet):
    serializer_class = serializers.ShipSerializer

    def get_queryset(self):
        queryset = models.Company.objects.prefetch_related('ownerships__ship')
        company = get_object_or_404(queryset, pk=self.kwargs['pk'])
        return company.ships.all()

    def retrieve_model(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class Ship(HalRetrieveModelMixin, GenericViewSet):
    queryset = models.Ship.objects.all()
    lookup_field = 'imo'
    serializer_class = serializers.ShipSerializer


class ShipOwnership(HalRetrieveModelMixin, GenericViewSet):
    queryset = models.ShipOwnership.objects.all()
    serializer_class = serializers.ShipOwnershipSerializer


class ShipOwnershipHistory(ListModelMixin, GenericViewSet):
    lookup_field = 'imo'
    serializer_class = serializers.ShipOwnershipSerializer

    def get_queryset(self):
        return models.ShipOwnership.objects.filter(ship__imo=self.kwargs['imo']).select_related('company', 'ship')

    def retrieve_model(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CompanyOwnershipHistory(ListModelMixin, GenericViewSet):
    serializer_class = serializers.ShipOwnershipSerializer

    def get_queryset(self):
        return models.ShipOwnership.objects.filter(company__pk=self.kwargs['pk']).select_related('company', 'ship')

    def retrieve_model(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
