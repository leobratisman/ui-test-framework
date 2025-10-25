from playwright.sync_api import Page
import allure

from components.base import BaseComponent
from components.dashboard.base_widget import WidgetWithChart


class WidgetsList(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.students_widget = WidgetWithChart(page=self._page, identifier="students")
        self.activities_widget = WidgetWithChart(page=self._page, identifier="activities")
        self.courses_widget = WidgetWithChart(page=self._page, identifier="courses")
        self.scores_widget = WidgetWithChart(page=self._page, identifier="scores")

    @allure.step("Checking dashboard widgets are visible")
    def check_visible(self):
        self.students_widget.check_visible()
        self.activities_widget.check_visible()
        self.courses_widget.check_visible()
        self.scores_widget.check_visible()