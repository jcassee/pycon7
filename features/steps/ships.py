from behave import *
from django.core.urlresolvers import reverse

from ship_registry.models import Company, Ship


@given("the registry contains no ships")
def step_impl(context):
    Ship.objects.all().delete()


@given('a ship named "{name}" with imo "{imo:d}"')
def step_impl(context, name, imo):
    company = Company.objects.create(name="{}'s owner".format(name))
    Ship.objects.create(name=name, imo=imo, owner=company)


@given('a ship named "{name}" with imo "{imo:d}" owned by "{owner}"')
def step_impl(context, name, imo, owner):
    company = Company.objects.get(name=owner)
    Ship.objects.create(name=name, imo=imo, owner=company)


@when('you get the ship "{name}"')
def step_impl(context, name):
    ship = Ship.objects.get(name=name)
    url = reverse('ship-detail', kwargs={'imo': ship.imo})
    context.execute_steps('when you get the resource at "{}"'.format(url))
