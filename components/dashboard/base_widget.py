from playwright.sync_api import Page
from typing import Literal
import allure

from components.base import BaseComponent
from elements import Image, Text


TITLES_LITERAL = Literal["students", "activities", "courses", "scores"]
LINKED_CHART_IDS: dict[TITLES_LITERAL, str] = {
    "students": "students-bar",
    "activities": "activities-line",
    "courses": "courses-pie",
    "scores": "scores-scatter"
}


class WidgetWithChart(BaseComponent):
    def __init__(self, page: Page, identifier: TITLES_LITERAL):
        super().__init__(page)
        self.__identifier = identifier

    @property
    def chart(self) -> Image:
        return Image(self._page, f"{LINKED_CHART_IDS[self.__identifier]}-chart", f"{self.__identifier.capitalize()} chart")
    
    @property
    def title(self) -> Text:
        return Text(self._page, f"{self.__identifier}-widget-title-text", f"{self.__identifier.capitalize()} title")
    
    @allure.step("Checking widget with chart is visible")
    def check_visible(self):
        with allure.step(f"Checking {self.__identifier} widget is visible"):
            self.title.check_visible()
            self.title.check_have_text(self.__identifier.capitalize())
            self.chart.check_visible()