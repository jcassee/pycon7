from behave import *
from django.core.urlresolvers import reverse

from ship_registry.models import Company, Ship


@given("the registry contains no ships")
def step_impl(context):
    Ship.objects.all().delete()


@given('a ship named "{name}" with imo "{imo:d}"')
def step_impl(context, name, imo):
    Ship.objects.create(name=name, imo=imo)


@given('a ship named "{name}" with imo "{imo:d}" owned by "{owner}"')
def step_impl(context, name, imo, owner):
    company = Company.objects.get(name=owner)
    Ship.objects.create(name=name, imo=imo, owner=company)


@when('you get the ship "{name}"')
def step_impl(context, name):
    ship = Ship.objects.get(name=name)
    url = reverse('ship', kwargs={'imo': ship.imo})
    context.execute_steps('when you get the resource at "{}"'.format(url))


@when('you search the registry with query "{query}"')
def step_impl(context, query):
    context.execute_steps(
        '''
        When you get the resource at "https://api.registronavale.com"
         And you follow the relation "http://rels.registronavale.com/search-ships" with parameters
             | param | value      |
             | q     | %s |
        ''' % query
    )
