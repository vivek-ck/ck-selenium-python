
from src.utils.base_class import BaseClass

class SalesforceLoginPage(BaseClass):
    URL = "https://cloudkaptanconsultancyse-3f-dev-ed.lightning.force.com/lightning/page/home"
    USERNAME_FIELD = "//input[@id='username']"
    PASSWORD_FIELD = "//input[@id='password']"
    LOGIN_BUTTON = "//input[@id='Login']"
        
    def open_page(sb):
        sb.open(SalesforceLoginPage.URL)

    def login(sb, username, password):
        sb.type(SalesforceLoginPage.USERNAME_FIELD, username)
        sb.type(SalesforceLoginPage.PASSWORD_FIELD, password)
        sb.click(SalesforceLoginPage.LOGIN_BUTTON)