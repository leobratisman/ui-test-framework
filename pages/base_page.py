from playwright.sync_api import Page, expect
import allure

from enums import PageUrlEnum


class BasePage:
    def __init__(self, page: Page):
        self._page = page
        self.wait_for_page_loaded()

    @property
    def url(self) -> str:
        return self._page.url
    
    @allure.step("Check that current page's URL equals to {url}")
    def check_url(self, url: PageUrlEnum):
        expect(self._page).to_have_url(url)

    @allure.step("Reloading page")
    def reload_page(self):
        self._page.reload(wait_until="domcontentloaded")

    @allure.step("Opening url - {url}")
    def visit(self, url: str):
        self._page.goto(url=url, wait_until="networkidle")

    def wait_for_page_loaded(self):
        self._page.wait_for_load_state("networkidle")