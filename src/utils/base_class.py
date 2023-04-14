from seleniumbase import BaseCase
#from selenium import webdriver

'''
This is an intermediate python file which imports all the features from "seleniumbase BaseCase".
The purpose of this file is to make small modifications to the methods present in "BaseCase" class
according to the user's need without changin the SeleniumBase package.

Feel free to override any methods as needed...

Happy Testing!!!
'''

class BaseClass(BaseCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # def get_new_driver(self, *args, **kwargs) :
    #     """This method overrides get_new_driver() from BaseCase."""
    #     options = webdriver.ChromeOptions()
    #     options.add_argument("--disable-3d-apis")
    #     options.add_argument("--disable-notifications")
    #     if self.headless:
    #         options.add_argument("--headless=new")
    #         options.add_argument("--disable-gpu")
    #     options.add_experimental_option(
    #         "excludeSwitches", ["enable-automation", "enable-logging"],
    #     )
    #     prefs = {
    #         "credentials_enable_service": False,
    #         "profile.password_manager_enabled": False,
    #     }
    #     options.add_experimental_option("prefs", prefs)
    #     return webdriver.Chrome(options=options)

    