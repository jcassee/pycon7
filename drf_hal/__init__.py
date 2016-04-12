import re

from rest_framework.views import exception_handler


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
