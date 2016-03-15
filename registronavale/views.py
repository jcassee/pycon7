from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse

import registronavale


@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request):
    return Response({
        'version': registronavale.__version__,
        '_links': {
            'self': {
                'href': request._request.get_raw_uri(),
            },
            'get-ship': {
                'href': reverse('ship-detail', kwargs={'imo': 'IMO'}, request=request).replace('IMO', '{imo}'),
            },
            'search-ships': {
                'href': reverse('ship-search', request=request) + "{?q}",
            },
        },
    })
