import requests
from behave import given, when, then

import payLoad
from Miscellanous import response
from utilities.configurations import getConfig, getPassword
from utilities.resources import ApiResources


@given('The Book details which need to be added to Library')
def step_impl(context):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    # Here we are assigning a property of URL to the Context object
    context.headers = {'Content-Type': 'application/json'}
    context.payLoad = payLoad.addBookPayload("BCR600", "ASDF")


@when('We execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payLoad, headers=context.headers, )


@then('Book is successfully added')
def step_impl(context):
    print(context.response.status_code)
    print(context.response.json())
    # Here we are converting response to json format
    response_json = context.response.json()
    print(type(response_json))
    context.bookID = response_json['ID']
    print(context.bookID)
    assert response_json['Msg'] == "successfully added"


@given('The Book details with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {'Content-Type': 'application/json'}
    context.payLoad = payLoad.addBookPayload(isbn, aisle)


# ==================================================

@given('I have github credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = ("mrinmoy.blr@gmail.com", getPassword())


@when('I hit getRepo API of github')
def step_impl(context):
    context.response = context.se.get(ApiResources.githubRepo)


@then('Status Code of response should be {statusCode:d}')
def step_impl(context, statusCode):
    print(statusCode)
    print(context.response.status_code)
    assert context.response.status_code == statusCode
