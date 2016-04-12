from rest_framework import permissions
from rest_framework.response import Response

import registronavale
from drf_hal import reverse
from drf_hal.views import HypermediaViewSet, HypermediaRetrieveMixin
from ship_registry import views as ship_views
from . import relations
from . import serializers


class ApiRoot(HypermediaRetrieveMixin, HypermediaViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.ApiRootSerializer

    def get_data(self, request):
        return {
            'version': registronavale.__version__,
        }
