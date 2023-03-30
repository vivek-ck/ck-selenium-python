from seleniumbase import BaseCase

class BaseClass(BaseCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)