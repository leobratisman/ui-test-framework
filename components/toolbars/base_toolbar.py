from playwright.sync_api import Page, Locator
from typing import Literal

from components.base import BaseComponent
from elements import Text

TOOLBARS_IDS_LITERAL = Literal["create-course", "dashboard", "courses-list", "create-course-exercises-box"] 


class BaseToolbar(BaseComponent):
    def __init__(
            self, 
            page: Page, 
            identifier: TOOLBARS_IDS_LITERAL
        ):
        super().__init__(page)
        self.__identifier = identifier

    @property
    def title(self) -> Text:
        return Text(self._page, f"{self.__identifier}-toolbar-title-text", "Toolbar title")