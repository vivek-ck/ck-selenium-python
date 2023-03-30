from seleniumbase.behave.behave_sb import *


def before_scenario(context, scenario):
    sb_config.behave_context = context
    sb_config.behave_scenario = scenario
    sb_config.behave_line_num = scenario.line
    sb_config.behave_step_count = 0
    context.sb.setUp()
    #context.sb.set_window_size(1280, 720)

def after_step(context, step):
    sb_config.behave_step = step
    if step.status == "failed":
        number = sb_config.behave_step_count
        print(">>> STEP FAILED:  (#%s) %s" % (number, step.name))
        print("Class / Feature: ", sb_config.behave_feature.name)
        print("Test / Scenario: ", sb_config.behave_scenario.name)
    context.sb.save_screenshot_to_logs()