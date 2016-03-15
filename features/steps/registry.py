import json

from behave import *
from django.core.urlresolvers import reverse
from uritemplate import expand

from ship_registry.models import Company, Ship


@given("the registry contains no ships")
def step_impl(context):
    Ship.objects.all().delete()


@given('a company named {name}')
def step_impl(context, name):
    Company.objects.create(name=name)


@given('a ship named "{name}" with imo "{imo}" owned by {owner}')
def step_impl(context, name, imo, owner):
    company = Company.objects.get(name=owner)
    Ship.objects.create(name=name, imo=imo, owner=company)


@when('you send a GET request to "{url}"')
def step_impl(context, url):
    context.response = context.test.client.get(url)


@when('you send a GET request to the root resource')
def step_impl(context):
    root_url = reverse('api-root')
    context.execute_steps('when you send a GET request to "{}"'.format(root_url))


@when('you follow the link relation "{rel}"')
def step_impl(context, rel):
    data = json.loads(context.response.content.decode())
    url = data['_links'][rel]['href']
    context.execute_steps('when you send a GET request to "{}"'.format(url))


@when('you follow the link relation "{rel}" with parameters')
def step_impl(context, rel):
    data = json.loads(context.response.content.decode())
    template = data['_links'][rel]['href']
    vars = parse_param_table(context.table)
    url = expand(template, var_dict=vars)
    context.execute_steps('when you send a GET request to "{}"'.format(url))


@then('the status is "{status}"')
def step_impl(context, status):
    assert str(context.response.status_code) == status, [context.response.status_code, status]


@then('the "{header}" header is "{value}"')
def step_impl(context, header, value):
    assert context.response[header] == value, [header, context.response[header], value]


@then('the JSON response contains')
def step_impl(context):
    expected = json.loads(context.text)
    actual = json.loads(context.response.content.decode())
    for key in list(actual.keys()):
        if key not in expected:
            del actual[key]
    assert actual == expected, [actual, expected]


def parse_param_table(table):
    result = {}
    for row in table.rows:
        result[row['param']] = row['value']
    return result
