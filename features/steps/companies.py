from behave import *
from rest_framework.reverse import reverse

from ship_registry.models import Company


@given('a company named "{name}"')
def step_impl(context, name):
    Company.objects.create(name=name)


@when('you get the company "{name}"')
def step_impl(context, name):
    company = Company.objects.get(name=name)
    url = reverse('company', kwargs={'pk': company.pk})
    context.execute_steps('when you get the resource at "{}"'.format(url))
