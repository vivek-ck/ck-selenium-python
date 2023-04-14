from .salesforce._login_page import LoginPage
from .salesforce._home_page import HomePage
from .salesforce._leads_page import LeadsPage
from src.utils import BaseKeywordManager

class SalesForce(BaseKeywordManager):

    def __init__(self) -> None:
        super().__init__("salesforce")

    def login_page():
        return LoginPage()
    def home_page():
        return HomePage()
    def leads_page():
        return LeadsPage()