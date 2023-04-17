from exceptiongroup import catch
from seleniumbase.behave.behave_sb import *
from allure_commons._allure import attach
from allure_commons.types import AttachmentType


'''
This is an intermediate python file which imports all the features from "seleniumbase.behave.behave_sb".
The purpose of this file is to make small modifications to the methods present in "behave_sb" according 
to the user's need without changin the SeleniumBase package.

Feel free to override any methods as needed...

Happy Testing!!!
'''

def after_step(context, step):
    sb_config.behave_step = step
    status = "FAILED"
    if step.status == "passed":
        status = "PASSED"

    number = sb_config.behave_step_count
    print(f">>> STEP {status}:  (#%s) %s" % (number, step.name))
    print("Class / Feature: ", sb_config.behave_feature.name)
    print("Test / Scenario: ", sb_config.behave_scenario.name)
    try:
        context.sb.wait_for_ready_state_complete(5)
        attach(context.sb.driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
    except :
        pass

