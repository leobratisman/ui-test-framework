from playwright.sync_api import Page
from typing import Literal

from components.base import BaseComponent
from elements import Icon, Text


class EmptyView(BaseComponent):
    def __init__(
            self, 
            page: Page, 
            identifier: Literal["courses-list", "create-course-preview", "create-course-exercises"]
        ):
        super().__init__(page)
        self.__identifier = identifier

    @property
    def icon(self) -> Icon:
        return Icon(self._page, f"{self.__identifier}-empty-view-icon", "Empty view icon")

    @property
    def title(self) -> Text:
        return Text(self._page, f"{self.__identifier}-empty-view-title-text", "Empty view title")

    @property
    def description(self) -> Text:
        return Text(self._page, f"{self.__identifier}-empty-view-description-text", "Empty view description")