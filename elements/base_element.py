from playwright.sync_api import Page, Locator, expect
import allure


class BaseElement:
    def __init__(self, page: Page, selector: str, name: str, by_test_id: bool = True):
        self._page = page
        self._selector = selector
        self._name = name
        self.__by_test_id = by_test_id

    def type_of(self) -> str:
        return "base element"

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        with allure.step(f'Getting locator with selector "{self._selector}" at index {nth}'):
            selector = self._selector.format(**kwargs)
            if not self.__by_test_id:
                return self._page.locator(selector)
            return self._page.get_by_test_id(selector).nth(nth)
    
    def click(self, nth: int = 0, **kwargs):
        with allure.step(f'Click {self.type_of()} with name "{self._name}"'):
            locator = self.get_locator(nth, **kwargs)
            locator.click()

    def hover(self, nth: int = 0, **kwargs):
        with allure.step(f'Hover {self.type_of()} with name "{self._name}"'):
            locator = self.get_locator(nth, **kwargs)
            locator.hover()

    def check_visible(self, nth: int = 0, **kwargs):
        with allure.step(f'Check that {self.type_of()} "{self._name}" is visible'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        with allure.step(f'Check that {self.type_of()} "{self._name}" has text "{text}"'):
            locator = self.get_locator(nth, **kwargs)
            expect(locator).to_have_text(text)
