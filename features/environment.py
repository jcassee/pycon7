def before_scenario(context, scenario):
    context.request_kwargs = {
        'SERVER_NAME': 'api.registronavale.com',
        'SERVER_PORT': str('443'),
        'wsgi.url_scheme': str('https'),
    }
