from playwright.sync_api import Page
from typing import Literal
import allure

from components.base import BaseComponent
from elements import Button, Icon, Text

from enums import PageUrlEnum


class SidebarListItemComponent(BaseComponent):
    def __init__(
        self, 
        page: Page, 
        identifier: Literal["dashboard", "courses", "logout"]
    ):
        super().__init__(page)
        self.__identifier = identifier
        self.__navigate_expected_url = self.get_expected_url(self.__identifier)

    @staticmethod
    def get_expected_url(
        identifier: Literal["dashboard", "courses", "logout"]
    ) -> PageUrlEnum:
        links = {
            "dashboard": PageUrlEnum.DASHBOARD_PAGE_URL,
            "courses": PageUrlEnum.COURSES_PAGE_URL,
            "logout": PageUrlEnum.LOGIN_PAGE_URL
        }
        return links[identifier]

    @property
    def button(self) -> Button:
        return Button(self._page, f"{self.__identifier}-drawer-list-item-button", f"{self.__identifier.capitalize()} item button")

    @property
    def icon(self) -> Icon:
        return Icon(self._page, f"{self.__identifier}-drawer-list-item-icon", f"{self.__identifier.capitalize()} item icon")
    
    @property
    def text(self) -> Text:
        return Text(self._page, f"{self.__identifier}-drawer-list-item-title-text", f"{self.__identifier.capitalize()} item text")
    
    @allure.step("Checking sidebar list item is visible")
    def check_visible(
        self, 
        text: Literal["Dashboard", "Courses", "Logout"]
    ):
        self.button.check_visible()
        self.icon.check_visible()
        self.text.check_visible()
        self.text.check_have_text(text)

    def navigate(self):
        with allure.step(f'Click {self.button.type_of()} "{self.button._name}" and navigate to {self.__navigate_expected_url}'):
            self.button.click()
            self.expected_url(url=self.__navigate_expected_url)
