''' Step definition for pet_id.feature'''
# pylint: disable=consider-using-f-string
import re
import json
from behave import step, then
from settings import API_URL, log


@then('this dog is named "{name}"')
def step_impl(context, name):
    data = context.response.json()
    import pdb; pdb.set_trace
    assert data['name'] == name, 'Expected dog named {expected}, but got {result}'.format(
        expected=name,
        result=data['name']
    )


@then('this dog\'s status is "{status}"')
def step_impl(context, status):
    data = context.response.json()
    import pdb; pdb.set_trace
    assert data['status'] == status, 'Expected dog to be {expected}, but it is {result}'.format(
        expected=status,
        result=data['status']
    )


@step('I POST "{uri}" to create a "{pet_type}" named "{name}" with an ID of "{pet_id:d}"')
def step_impl(context, uri, pet_type, name, pet_id):
    context.current_url = API_URL + uri
    body = {
        "id": pet_id,
        "name": name,
        "category": {
            "id": 1,
            "name": pet_type
        },
        "photoUrls": [
            "https://www.rd.com/wp-content/uploads/2019/12/GettyImages-978939420.jpg"
        ],
        "tags": [
            {
            "id": 0,
            "name": "new"
            }
        ],
        "status": "available"
    }
    log.debug('Posting to url with requests %s', context.current_url)
    context.response = context.session.post(
        context.current_url,
        json=body
    )

