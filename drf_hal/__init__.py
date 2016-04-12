from rest_framework.reverse import reverse as rest_reverse

def reverse(view, args=None, kwargs=None, request=None, format=None, **extra):
    if hasattr(view, 'get_view_name'):
        view = view.get_view_name()
    return rest_reverse(view, args, kwargs, request, format, **extra)
