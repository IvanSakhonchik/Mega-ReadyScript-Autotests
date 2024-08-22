from framework.elements.BaseElement import BaseElement


class BaseForm:
    def __init__(self, locator, name):
        self.default_element = BaseElement(locator, name)

    def is_page_opened(self):
        return self.default_element.is_visible()

    def is_page_closed(self):
        return self.default_element.is_hidden()
