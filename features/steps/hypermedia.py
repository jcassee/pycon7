import json

import re
from behave import *
from django.core.urlresolvers import reverse
from uritemplate import expand

from ship_registry.models import Company, Ship


@when('you get the resource at "{url}"')
def step_impl(context, url):
    context.response = context.test.client.get(url, **context.request_kwargs)
    context.response_text = context.response.content.decode()


@when('you follow the relation "{rel}"')
@when('you follow the relation "{rel}" with parameters')
def step_impl(context, rel):
    data = json.loads(context.response_text)

    try:
        embedded = data['_embedded'][rel]
        assert context.table is None, 'trying to follow embedded relation with parameters: %s' % rel
        context.response_text = json.dumps(embedded)
        return
    except KeyError:
        pass

    try:
        url = data['_links'][rel]['href']
    except KeyError:
        assert False, context.response_text

    var_dict = parse_param_table(context.table)
    if var_dict:
        url = expand(url, var_dict)
    context.execute_steps('when you get the resource at "{}"'.format(url))


@when('you follow the embedded relation "{rel}"')
def step_impl(context, rel):
    data = json.loads(context.response_text)
    try:
        embedded = data['_embedded'][rel]
    except KeyError:
        assert False, context.response_text
    context.response_text = json.dumps(embedded)


@when('you take the {ordinal} resource')
def step_impl(context, ordinal):
    if ordinal == 'first':
        index = 0
    elif ordinal == 'last':
        index = -1
    else:
        index = int(re.search(r'\d+', ordinal).group()) - 1
    context.execute_steps('when you take resource {}'.format(index))


@when('you take resource {index}')
def step_impl(context, index):
    data = json.loads(context.response_text)
    try:
        element = data[int(index)]
    except KeyError:
        assert False, context.response_text
    context.response_text = json.dumps(element)


@then('the status is "{status}"')
def step_impl(context, status):
    actual = str(context.response.status_code)
    assert actual == status, actual


@then('the "{header}" header is "{expected}"')
def step_impl(context, header, expected):
    actual = context.response[header]
    assert actual == expected, actual


@then('the profile is "{expected}"')
def step_impl(context, expected):
    pass


@then('the representation is')
def step_impl(context):
    expected = json.loads(context.text)
    actual = json.loads(context.response_text)
    assert actual == expected, context.response_text


@then('the representation contains')
def step_impl(context):
    expected = json.loads(context.text)
    actual = json.loads(context.response_text)
    for key in list(actual.keys()):
        if key not in expected:
            del actual[key]
    assert actual == expected, context.response_text


def parse_param_table(table):
    result = {}
    for row in table.rows:
        result[row['param']] = row['value']
    return result
