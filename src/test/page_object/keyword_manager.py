from src.test.page_object.salesforce.login_page import SalesforceLoginPage
from src.test.page_object.salesforce.home_page import SalesforceHomePage
from src.test.page_object.salesforce.leads_page import SalesforceLeadsPage

class KeywordManager():
    def salesforce_login_page():
        return SalesforceLoginPage
    def salesforce_home_page():
        return SalesforceHomePage
    def salesforce_leads_page():
        return SalesforceLeadsPage
    
