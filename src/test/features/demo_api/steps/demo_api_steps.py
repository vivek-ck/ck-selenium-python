from email import header
import json
from xml.etree.ElementTree import tostring
import requests
from behave import given, when, then

# Define the API endpoint variable
api_endpoint = ''

# Define the payload variable
payload = {}

@given('I have the API endpoint "{endpoint}"')
def step_impl(context, endpoint):
    global api_endpoint
    api_endpoint = endpoint

@when('I send a GET request')
def step_impl(context):
    global api_endpoint
    context.response = requests.get(api_endpoint)

@when('I send a POST request')
def step_impl(context):
    global api_endpoint, payload
    context.response = requests.post(api_endpoint, json=payload)

@given('I use the payload from file {filename:S}')
def step_impl(context, filename):
    global payload
    with open("resources/payload_json/" + filename) as f:
        payload = json.load(f)
    print(payload)

@then('the response status code should be {status_code}')
def step_impl(context, status_code):
    assert context.response.status_code == int(status_code), "Expected: " + status_code + " but got: " + str(context.response.status_code)


@then('the response body should contain a list of posts')
def step_impl(context):
    response_data = context.response.json()
    assert isinstance(response_data, list)
    assert len(response_data) > 0

@then('the response body should contain a single post')
def step_impl(context):
    response_data = context.response.json()
    assert isinstance(response_data, dict)
    assert response_data.get('id') == 1

@then('the response body should contain the newly created post')
def step_impl(context):
    response_data = context.response.json()
    assert isinstance(response_data, dict)
    assert response_data.get('title') == payload.get('title'), response_data.get('title')
    assert response_data.get('body') == payload.get('body'), response_data.get('body')
    assert response_data.get('userId') == payload.get('userId'), response_data.get('userId')