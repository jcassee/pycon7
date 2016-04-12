from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet

import registronavale
from drf_hal.views import HalRetrieveMixin
from . import serializers


class ApiRoot(HalRetrieveMixin, GenericViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.ApiRootSerializer

    def get_data(self, request):
        return {
            'version': registronavale.__version__,
        }
