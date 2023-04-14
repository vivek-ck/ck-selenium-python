
from src.utils import BaseClass

class LoginPage():
    URL = "https://cloudkaptanconsultancyse-3f-dev-ed.lightning.force.com/lightning/page/home"
    USERNAME_FIELD = "//input[@id='username']"
    PASSWORD_FIELD = "//input[@id='password']"
    LOGIN_BUTTON = "//input[@id='Login']"
        
    def open_page(self, sb: BaseClass):
        sb.open(self.URL)

    def login(self, sb: BaseClass, username, password):
        sb.type(self.USERNAME_FIELD, username)
        sb.type(self.PASSWORD_FIELD, password)
        sb.click(self.LOGIN_BUTTON)