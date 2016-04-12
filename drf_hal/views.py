import re

from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import exception_handler

from drf_hal.renderers import HalJsonRenderer


class HypermediaViewSet(GenericViewSet):
    view_name = None
    renderer_classes = [HalJsonRenderer]

    @classmethod
    def get_view_name(cls):
        if cls.view_name is not None:
            return cls.view_name
        else:
            return classname_to_viewname(cls.__name__)


class HypermediaRetrieveMixin(object):
    def retrieve(self, request, *args, **kwargs):
        data = self.get_data(request)
        serializer = self.get_serializer(data=data)
        return Response(serializer.get_initial())

    def get_data(self, request):
        raise NotImplementedError('`get_data()` must be implemented')


class HypermediaRetrieveModelMixin(object):
    def retrieve_model(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


def vnderror_exception_handler(exc, context):
    ret = exception_handler(exc, context)
    if hasattr(ret, 'content_type'):
        ret.content_type = 'application/vnd.error+json'
    return ret


# http://stackoverflow.com/a/1176023
_first_cap_re = re.compile(r'(.)([A-Z][a-z]+)')
_all_cap_re = re.compile(r'([a-z0-9])([A-Z])')
def classname_to_viewname(word):
    s1 = _first_cap_re.sub(r'\1-\2', word)
    return _all_cap_re.sub(r'\1-\2', s1).lower()
