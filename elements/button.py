from playwright.sync_api import expect
import allure

from elements.base_element import BaseElement


class Button(BaseElement):
    def type_of(self) -> str:
        return "button"

    def check_disabled(self, nth: int = 0, **kwargs):
        with allure.step(f'Check that button "{self._name}" is disabled'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_disabled()

    def check_enabled(self, nth: int = 0, **kwargs):
        with allure.step(f'Check that button "{self._name}" is enabled'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).not_to_be_disabled()
