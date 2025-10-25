from playwright.sync_api import Page
import allure

from components.base import BaseComponent
from elements import Text


class Navbar(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def title(self) -> Text:
        return Text(self._page, "navigation-navbar-app-title-text", "Navbar title")
    
    @property
    def welcome_text(self) -> Text:
        return Text(self._page, "navigation-navbar-welcome-title-text", "Navbar welcome text")
    
    @allure.step("Checking navbar is visible")
    def check_visible(self, username: str):
        self.title.check_visible()
        self.title.check_have_text("UI Course")

        self.welcome_text.check_visible()
        self.welcome_text.check_have_text(f"Welcome, {username}!")

