import logging

'''
This is an intermediate the base of all KeywordManager classes. All KeywordManagers are expected to inherit this class.
A KeywordManager is used to provide a quick and organized access to pageobject methods.

Any essential or quality of life features that can be added to KeywordManager classes should be added through this class.

Happy Testing!!!
'''

class BaseKeywordManager() :
    def __init__(self, module_name) -> None:
        logging.info("KeywordManager has been initialized for: " + module_name)