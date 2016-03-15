from behave import *
from django.core.urlresolvers import reverse


@when('you get the root resource')
def step_impl(context):
    root_url = reverse('api-root')
    context.execute_steps('when you get the resource at "{}"'.format(root_url))
