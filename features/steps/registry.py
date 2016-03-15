from behave import *


@given('the API is available')
def step_impl(context):
    pass


@when('you send a GET request to "{url}"')
def step_impl(context, url):
    pass


@then('the status is "{status}"')
def step_impl(context, status):
    pass


@then('the "{header}" header is "{value}"')
def step_impl(context, header, value):
    pass


@then('the JSON response contains')
def step_impl(context):
    pass


@step("the registry contains no ships")
def step_impl(context):
    pass


@step('a ship named "{name}" with imo "{imo}"')
def step_impl(context, name, imo):
    pass

@step('you follow the link relation "{rel}"')
def step_impl(context, rel):
    pass


@step('you follow the link relation "{rel}" with parameters')
def step_impl(context, rel):
    pass
