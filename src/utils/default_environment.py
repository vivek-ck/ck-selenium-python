from src.utils.base_class import BaseClass
from src.utils import base_behave_sb
base_behave_sb.set_base_class(BaseClass)  # Accepts a BaseCase subclass
from src.utils.base_behave_sb import before_all  # noqa
from src.utils.base_behave_sb import before_feature  # noqa
from src.utils.base_behave_sb import before_scenario  # noqa
from src.utils.base_behave_sb import before_step  # noqa
from src.utils.base_behave_sb import after_step  # noqa
from src.utils.base_behave_sb import after_scenario  # noqa
from src.utils.base_behave_sb import after_feature  # noqa
from src.utils.base_behave_sb import after_all  # noqa

'''
In Behave, environment.py is a special file that is automatically loaded before any feature file is executed. 
It provides a way to define custom code that is executed at various points in the testing process. 
Some of the common uses of environment.py in SeleniumBase include:

    1) Setting up and tearing down the test environment
    2) Initializing and closing the Selenium driver
    3) Defining custom command line options and environment variables
    4) Creating custom fixtures that can be used across multiple feature files

This file is being imported by environment.py under different Behave Feature locations, e.g., features/demo_api/environment.py

########################################################################################################################################################
Example:

    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait

    from seleniumbase import config as sb_config


    def before_all(context):
        # Set up the Selenium driver
        options = Options()
        options.add_argument("--start-maximized")
        context.driver = webdriver.Chrome(options=options)


    def after_all(context):
        # Clean up the Selenium driver
        context.driver.quit()


    def before_feature(context, feature):
        # Load the base URL before each feature file
        context.driver.get(sb_config.get_base_url())


    def after_scenario(context, scenario):
        # Take a screenshot after each scenario
        context.driver.save_screenshot(f"screenshots/{scenario.name}.png")


    def before_step(context, step):
        # Wait for the element to be visible before each step
        WebDriverWait(context.driver, 10).until(lambda driver: driver.find_element(*step.location))


    def after_step(context, step):
        # Clear the input field after each step
        if "input" in step.name.lower():
            input_field = context.driver.find_element(*step.location)
            input_field.send_keys(Keys.CONTROL, "a")
            input_field.send_keys(Keys.BACKSPACE)


    # Define a custom fixture
    def create_user(context, username, password):
        context.driver.get("https://example.com/register")
        context.driver.find_element_by_id("username").send_keys(username)
        context.driver.find_element_by_id("password").send_keys(password)
        context.driver.find_element_by_id("register-button").click()


    # Register the custom fixture
    def before_scenario(context, scenario):
        context.create_user = create_user

########################################################################################################################################################

Happy Testing!!!
'''