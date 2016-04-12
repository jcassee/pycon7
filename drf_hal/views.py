from rest_framework.response import Response


class HalRetrieveMixin(object):
    def retrieve(self, request, *args, **kwargs):
        data = self.get_data(request)
        serializer = self.get_serializer(data=data)
        return Response(serializer.get_initial())

    def get_data(self, request):
        raise NotImplementedError('`get_data()` must be implemented')


class HalRetrieveModelMixin(object):
    def retrieve_model(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
