'''Shared steps for all tests'''
# pylint: disable=missing-function-docstring,attribute-defined-outside-init,consider-using-f-string,too-many-public-methods,function-redefined
import re
import requests
from behave import step, then
from custom_exceptions import loop_thru_messages
from settings import API_URL, log


@step('I "{method}" "{uri}" with requests')
def get(context, method, uri):
    context.current_url = API_URL + uri
    if method == "GET":
        log.debug('Getting this url with requests %s', context.current_url)
        context.response = context.session.get(
            context.current_url
        )


@step('I "{method}" "{uri}" with the parameters "{parameters}"')
def step_impl(context, method, uri, parameters):
    context.current_url = API_URL + uri + parameters
    if method == "GET":
        log.debug('Getting this url with requests %s', context.current_url)
        context.response = context.session.get(
            context.current_url
        )


@step('it should have a "{code:d}" status code')
def step_impl(context, code):
    assert context.response.status_code == code, \
    'Did not get {expected} status code on response, instead {result}'.format(
        expected = code,
        result = context.response.status_code
    )


@step('the response message should include "{message}"')
def step_impl(context, message):
    data = context.response.json()
    assert message in data['message'] , \
    'Expected {expected} to be in message, instead got {result}'.format(
        expected = message,
        result = data['message']
    )


@then('the response should use https')
def step_impl(context):
    regex = re.compile('^https:')
    assert regex.match(context.response.url), \
    'Expected the response to be on https, but got {url}'.format(
        url = context.response.url
    )

@step('the response data should include "{key}" of "{value}"')
def step_impl(context, key, value):
    data = context.response.json()
    assert value == data[key], \
    'Expected {expected} to be in response, instead got {result}'.format(
        expected = value,
        result = data[key]
    )

@step('the response data should include "{key}" number "{value:d}"')
def step_impl(context, key, value):
    data = context.response.json()
    assert value == data[key], \
    'Expected {expected} to be in response, instead got {result}'.format(
        expected = value,
        result = data[key]
    )

@then('the response should be returned in under "{expected_seconds:d}" seconds')
def step_impl(context, expected_seconds):
    assert context.response.elapsed.total_seconds() <= float(expected_seconds), \
        'The response took {} seconds'.format(context.response.elapsed)

