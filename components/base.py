from playwright.sync_api import Page, expect
import allure

from enums import PageUrlEnum

class BaseComponent:
    def __init__(self, page: Page):
        self._page = page

    @allure.step("Check that current page's URL equals to {url}")
    def expected_url(self, url: PageUrlEnum):
        expect(self._page).to_have_url(url)