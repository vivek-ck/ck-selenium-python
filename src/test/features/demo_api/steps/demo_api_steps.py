from email.mime import base
import json
import requests
from behave import step
from src.utils.file_paths import json_payload

# Save base url
base_url = ''
# Save payload
payload = ''


@step('I have the Base Url "{url}"')
def step_impl(context, url):
    global base_url
    base_url = url


@step('I use the payload from file "{filename}"')
def step_impl(context, filename):
    global payload
    with open(json_payload + filename) as f:
        payload = json.load(f)


@step('I have the API endpoint "{endpoint}"')
def step_impl(context, endpoint):
    context.endpoint = endpoint


@step('I send a GET request')
def step_impl(context):
    context.response = requests.get(context.endpoint)


@step('I send a POST request with the payload file "{filename}"')
def step_impl(context, filename):
    with open(json_payload + filename) as f:
        context.payload = json.load(f)
        context.response = requests.post(
            context.endpoint, json=context.payload)


@step('the response status code should be {status_code}')
def step_impl(context, status_code):
    assert context.response.status_code == int(
        status_code), f"Expected: {status_code}, but got: {context.response.status_code}"


@step('the response body should contain a list of {entity}')
def step_impl(context, entity):
    response_data = context.response.json()
    assert isinstance(
        response_data, list), f"Expected a list, but got {type(response_data)}"
    assert len(response_data) > 0, f"Expected a non-empty list of {entity}"


@step('the response body should contain a single {entity}')
def step_impl(context, entity):
    response_data = context.response.json()
    assert isinstance(
        response_data, dict), f"Expected a dictionary, but got {type(response_data)}"
    assert response_data.get(
        'id') == 1, f"Expected id: 1, but got id: {response_data.get('id')}"


@step('the response body should contain the newly created {entity}')
def step_impl(context, entity):
    response_data = context.response.json()
    payload = context.payload
    assert isinstance(
        response_data, dict), f"Expected a dictionary, but got {type(response_data)}"
    assert response_data.get('title') == payload.get(
        'title'), f"Expected title: {payload.get('title')}, but got title: {response_data.get('title')}"
    assert response_data.get('body') == payload.get(
        'body'), f"Expected body: {payload.get('body')}, but got body: {response_data.get('body')}"
    assert response_data.get('userId') == payload.get(
        'userId'), f"Expected userId: {payload.get('userId')}, but got userId: {response_data.get('userId')}"

# Reusable step implementation for sending a request and verifying the response


@step('I send a {method} request to the endpoint "{endpoint}" with the payload')
def step_impl(context, method, endpoint):
    context.endpoint = endpoint
    context.response = None
    context.payload = json.loads(context.text)
    if method == "GET":
        context.response = requests.get(context.endpoint)
    elif method == "POST":
        context.response = requests.post(
            context.endpoint, json=context.payload)
    else:
        raise ValueError(f"Unsupported method: {method}")


@step('the response body should contain {count:d} {entity}')
def step_impl(context, count, entity):
    response_data = context.response.json()
    assert isinstance(
        response_data, list), f"Expected a list, but got {type(response_data)}"
