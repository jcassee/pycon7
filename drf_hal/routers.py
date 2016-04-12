from rest_framework.routers import SimpleRouter, Route


class HypermediaRouter(SimpleRouter):
    routes = [
        Route(
            url=r'^{prefix}{trailing_slash}$',
            mapping={
                'get': 'retrieve',
                'put': 'update',
                'patch': 'partial_update',
                'post': 'process',
                'delete': 'destroy',
            },
            name='{basename}',
            initkwargs={},
        ),
        Route(
            url=r'^{prefix}/{lookup}{trailing_slash}$',
            mapping={
                'get': 'retrieve_model',
                'put': 'update_model',
                'patch': 'partial_update_model',
                'post': 'process_model',
                'delete': 'destroy_model',
            },
            name='{basename}',
            initkwargs={},
        ),
    ]
