from framework.elements.BaseElement import BaseElement


class TextField(BaseElement):
    def __init__(self, locator, name):
        super().__init__(locator, name)

    def send_keys(self, text):
        element = self.get_web_element()
        element.clear()
        element.send_keys(text)
