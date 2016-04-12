import link_header
from rest_framework import renderers
from rest_framework.reverse import reverse


class HalJsonRenderer(renderers.JSONRenderer):
    media_type = 'application/hal+json'

    def render(self, data, media_type=None, renderer_context=None):
        response = renderer_context['response']
        if response.content_type == 'application/vnd.error+json':
            self.enrich_vnd_error(data, renderer_context['request'])
        return super(HalJsonRenderer, self).render(data, media_type, renderer_context)

    def enrich_vnd_error(self, data, request):
        links = data.setdefault('_links', {})
        if 'about' not in links:
            links['about'] = {'href': request.build_absolute_uri()}
