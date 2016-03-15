from behave import *

from ship_registry.models import Company


@given('a company named "{name}"')
def step_impl(context, name):
    Company.objects.create(name=name)
