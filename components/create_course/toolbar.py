from playwright.sync_api import Page
import allure

from components.toolbars.base_toolbar import BaseToolbar
from elements import Button

from enums.page_url import PageUrlEnum


class CreateCourseToolbar(BaseToolbar):
    def __init__(self, page: Page):
        super().__init__(page, identifier="create-course")

    @property
    def create_course_button(self) -> Button:
        return Button(self._page, "create-course-toolbar-create-course-button", "Create course button")
    
    @allure.step("Checking create course is visible")
    def check_visible(self):
        self.create_course_button.check_visible()
        self.title.check_visible()
        self.title.check_have_text("Create course")

    @allure.step("Click create course button")
    def click_create_course_button(self):
        self.create_course_button.click()
        self.expected_url(PageUrlEnum.COURSES_PAGE_URL)