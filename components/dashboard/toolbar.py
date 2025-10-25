from playwright.sync_api import Page
import allure

from components.toolbars.base_toolbar import BaseToolbar


class DashboardToolbar(BaseToolbar):
    def __init__(self, page: Page):
        super().__init__(page, identifier="dashboard")

    @allure.step("Checking dashboard toolbar is visible")
    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text("Dashboard")