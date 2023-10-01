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
def get(context, method, uri, parameters):
    context.current_url = API_URL + uri + parameters
    if method == "GET":
        log.debug('Getting this url with requests %s', context.current_url)
        context.response = context.session.get(
            context.current_url
        )


@step('it should have a "{code:d}" status code')
def step_impl(context, code):
    assert context.response.status_code == code, \
    'Did not get {expected} status code on response, instead {resullt}'.format(
        expected = code,
        resullt = context.response.status_code
    )


@then('the response should use https')
def get(context):
    regex = re.compile('^https:')
    assert regex.match(context.response.url), \
    'Expected the response to be on https, but got {url}'.format(
        url = context.response.url
    )
