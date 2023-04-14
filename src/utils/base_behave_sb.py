from seleniumbase.behave.behave_sb import *


'''
This is an intermediate python file which imports all the features from "seleniumbase.behave.behave_sb".
The purpose of this file is to make small modifications to the methods present in "behave_sb" according 
to the user's need without changin the SeleniumBase package.

Feel free to override any methods as needed...

Happy Testing!!!
'''


def after_step(context, step):
    sb_config.behave_step = step
    if step.status == "failed":
        number = sb_config.behave_step_count
        print(">>> STEP FAILED:  (#%s) %s" % (number, step.name))
        print("Class / Feature: ", sb_config.behave_feature.name)
        print("Test / Scenario: ", sb_config.behave_scenario.name)
    context.sb.save_screenshot_to_logs()
