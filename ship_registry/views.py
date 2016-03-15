from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse

from . import models
from . import serializers


@api_view(['GET'])
@permission_classes([AllowAny])
def search_ships(request):
    query = request.query_params['q']
    ships = models.Ship.objects.filter(name__contains=query)
    serializer = serializers.ShipSerializer(ships, many=True, context={'request': request})
    return Response(serializer.data)
    return Response({
        '_links': {
            'self': {
                'href': reverse('ship-search', request=request),
            },
        },
        '_embedded': {
            'item': [serializers.ShipSerializer(ship, context={'request': request}).data for ship in ships]
        }
    })


class CompanyDetail(generics.RetrieveAPIView):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer


class ShipDetail(generics.RetrieveAPIView):
    lookup_field = 'imo'
    serializer_class = serializers.ShipSerializer

    def get_queryset(self):
        return models.Ship.objects.filter(imo=self.kwargs['imo'])
