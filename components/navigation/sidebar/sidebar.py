from playwright.sync_api import Page
import allure

from components.base import BaseComponent
from components.navigation.sidebar.sidebar_list_item import SidebarListItemComponent


class Sidebar(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def dashboard_button(self) -> SidebarListItemComponent:
        return SidebarListItemComponent(page=self._page, identifier="dashboard")
        
    @property
    def courses_button(self) -> SidebarListItemComponent:
        return SidebarListItemComponent(page=self._page, identifier="courses")    

    @property
    def logout_button(self) -> SidebarListItemComponent:
        return SidebarListItemComponent(page=self._page, identifier="logout")    

    @allure.step("Checking sidebar is visible")
    def check_visible(self):
        self.dashboard_button.check_visible(text="Dashboard")
        self.courses_button.check_visible(text="Courses")
        self.logout_button.check_visible(text="Logout")

    @allure.step("Click dashboard button")
    def click_to_dashboard_button(self):
        self.dashboard_button.navigate()

    @allure.step("Click courses button")
    def click_to_courses_button(self):
        self.courses_button.navigate()

    @allure.step("Click logout button")
    def click_logout_button(self):
        self.logout_button.navigate()