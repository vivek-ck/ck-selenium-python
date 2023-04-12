from behave import given, when, then
from src.test.page_object.keyword_manager import KeywordManager

@given("the Salesforce login page is opened")
def step_impl(context):
    KeywordManager.salesforce_login_page().open_page(context.sb)

@when("the user logs in with username {username:S} and password {password:S}")
def step_impl(context, username, password):
    KeywordManager.salesforce_login_page().login(context.sb, username, password)

@when('the user navigates to the Leads page')
def step_impl(context):
    KeywordManager.salesforce_home_page().click_leads_tab(context.sb)

@when('the user creates new lead with Salutation "{salutation}", LastName "{lastName}", Company "{company}"')
def step_impl(context, salutation, lastName, company):
    KeywordManager.salesforce_leads_page().initiate_lead(context.sb)
    KeywordManager.salesforce_leads_page().create_lead(context.sb, salutation, lastName, company)

@then('the Lead with name "{lastName}" should be present in the Leads list')
def step_impl(context, lastName):
    KeywordManager.salesforce_home_page().click_leads_tab(context.sb)
    KeywordManager.salesforce_leads_page().validate_lead(context.sb, lastName)