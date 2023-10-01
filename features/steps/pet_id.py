''' Step definition for pet_id.feature'''
# pylint: disable=consider-using-f-string
import re
import json
from behave import step, then
from settings import API_URL, log


@then('this dog is named "{name}"')
def get(context, name):
    data = context.response.json()
    import pdb; pdb.set_trace
    assert data['name'] == name, 'Expected dog named {expected}, but got {result}'.format(
        expected=name,
        result=data['name']
    )

@then('this dog\'s status is "{status}"')
def get(context, status):
    data = context.response.json()
    import pdb; pdb.set_trace
    assert data['status'] == status, 'Expected dog to be {expected}, but it is {result}'.format(
        expected=status,
        result=data['status']
    )

