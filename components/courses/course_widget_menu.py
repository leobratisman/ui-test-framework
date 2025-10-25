from playwright.sync_api import Locator, Page, expect

from components.base import BaseComponent
from elements import Link, Text, Icon


class CourseWidgetMenu(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

    # ------------- EDIT ---------------
    @property
    def course_menu_edit_item(self) -> Link:
        return Link(self._page, "course-view-edit-menu-item", "Menu edit button")
    
    @property
    def course_menu_edit_item_text(self) -> Text:
        return Text(self._page, "course-view-edit-menu-item-text", "Menu edit button text")
    
    @property
    def course_menu_edit_item_icon(self) -> Icon:
        return Icon(self._page, "course-view-edit-menu-item-icon", "Menu edit button icon")

    # ------------- DELETE ---------------
    @property
    def course_menu_delete_item(self) -> Link:
        return Link(self._page, "course-view-delete-menu-item", "Menu delete button")
    
    @property
    def course_menu_delete_item_text(self) -> Text:
        return Text(self._page, "course-view-delete-menu-item-text", "Menu delete button text")
    
    @property
    def course_menu_delete_item_icon(self) -> Icon:
        return Icon(self._page, "course-view-delete-menu-item-icon", "Menu delete button icon")

    # ------------- ACTIONS --------------
    def click_edit_item(self, index: int = 0):
        self.course_menu_edit_item.check_visible(nth=index)
        self.course_menu_edit_item.click(nth=index)

    def click_delete_item(self, index: int = 0):
        self.course_menu_delete_item.check_visible(nth=index)
        self.course_menu_delete_item.click(nth=index)