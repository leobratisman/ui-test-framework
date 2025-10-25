from playwright.sync_api import expect
import allure

from elements.base_element import BaseElement


class Input(BaseElement):
    def type_of(self) -> str:
        return "input"
    
    def get_locator(self, nth: int = 0, **kwargs):
        return super().get_locator(nth, **kwargs).locator("input")
    
    def check_disabled(self, nth: int = 0, **kwargs):
        with allure.step(f'Check that input "{self._name}" is disabled'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_disabled()

    def check_enabled(self, nth: int = 0, **kwargs):
        with allure.step(f'Check that input "{self._name}" is enabled'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).not_to_be_disabled()

    def get_value(self, nth: int = 0, **kwargs) -> str:
        locator = self.get_locator(nth, **kwargs)
        return locator.input_value()
    
    def check_have_value(self, value: str, nth: int = 0, **kwargs) -> str:
        with allure.step(f'Check that input "{self._name}" has value "{value}'):
            locator = self.get_locator(nth, **kwargs)
            return expect(locator).to_have_value(value)
    
    def fill(self, value: str, nth: int = 0, **kwargs):
        with allure.step(f'Fill "{value}" to "{self._name}" input'):
            locator = self.get_locator(nth, **kwargs)
            locator.fill(value)
