from playwright.sync_api import Page
import allure

from components.toolbars.base_toolbar import BaseToolbar
from enums.page_url import PageUrlEnum

from elements import Button


class CoursesToolbar(BaseToolbar):
    def __init__(self, page: Page):
        super().__init__(page, identifier="courses-list")

    @property
    def create_course_button(self) -> Button:
        return Button(self._page, "courses-list-toolbar-create-course-button", "Create course button")
    
    @allure.step("Checking courses toolbar is visible")
    def check_visible(self):
        self.create_course_button.check_visible()
        self.title.check_visible()
        self.title.check_have_text("Courses")

    @allure.step("Click create course button")
    def click_create_course_button(self):
        self.create_course_button.click()
        self.expected_url(PageUrlEnum.CREATE_COURSE_PAGE_URL)