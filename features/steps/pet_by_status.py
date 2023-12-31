''' Step definition for pet_by_status.feature'''
# pylint: disable=consider-using-f-string
import re
import json
from behave import step, then
from settings import API_URL, log


@then('the json response should be a list of least "{int:d}" items')
def step_impl(context, int):
    data = context.response.json()
    assert isinstance(data, list), 'Expected a but found {}'.format(type(data))
    assert len(data) >= int, 'List was {result} items, expected greater than {expected}'.format(
        result=len(data),
        expected=int
    )

@then('the json response should be a dict of least "{int:d}" items')
def step_impl(context, int):
    data = context.response.json()
    assert isinstance(data, dict), 'Expected a but found {}'.format(type(data))
    assert len(data) >= int, 'List was {result} items, expected greater than {expected}'.format(
        result=len(data),
        expected=int
    )


@then('the json response should contain a dog named "{name}"')
def step_impl(context, name):
    data = context.response.json()
    assert any(dog['name'] == name for dog in data), 'Did not find a dog named {}'.format(name)


@then('the json response should not contain a dog named "{name}"')
def step_impl(context, name):
    data = context.response.json()
    for dog in data:
        try:
            assert not dog['name'] == name, 'Unexpectedly found a dog named {}'.format(name)
        except KeyError:
            continue


@then('all dogs should have a name')
def step_impl(context):
    data = context.response.json()
    assert all('name' in dog for dog in data), 'A dog was missing the name key'


@then('all dogs should have an ID')
def step_impl(context):
    data = context.response.json()
    assert all('id' in dog for dog in data), 'A dog was missing ID data'


@then('all dogs should have a status')
def step_impl(context):
    data = context.response.json()
    assert all('status' in dog for dog in data), 'A dog was missing status data'


@then('should not reveal dog pii')
def step_impl(context):
    data = context.response.json()
    assert not any('dob' in dog for dog in data), 'Data should not include a dogs Personal Identifiable Information'
