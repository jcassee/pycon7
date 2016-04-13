def before_scenario(context, scenario):
    # Use real URLs in output
    context.request_kwargs = {
        'SERVER_NAME': 'api.registronavale.com',
        'SERVER_PORT': str('443'),
        'wsgi.url_scheme': str('https'),
    }
