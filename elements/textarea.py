from elements.input import Input
from elements.base_element import BaseElement


class Textarea(Input):
    def type_of(self) -> str:
        return "textarea"
    
    def get_locator(self, nth = 0, **kwargs):
        return BaseElement.get_locator(self, nth, **kwargs).locator("textarea").first