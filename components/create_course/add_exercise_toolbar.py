from playwright.sync_api import Page
import allure

from components.toolbars.base_toolbar import BaseToolbar
from enums.page_url import PageUrlEnum

from elements import Button


class AddExerciseToolbar(BaseToolbar):
    def __init__(self, page: Page):
        super().__init__(page, identifier="create-course-exercises-box")

    @property
    def add_exercise_button(self) -> Button:
        return Button(self._page, "create-course-exercises-box-toolbar-create-exercise-button", "Add exercise button")
    
    @allure.step("Checking add exercise toolbar is visible")
    def check_visible(self):
        self.add_exercise_button.check_visible()
        self.title.check_visible()
        self.title.check_have_text("Exercises")

    @allure.step("Click add exercise button")
    def click_add_exercise_button(self):
        self.add_exercise_button.click()
        self.expected_url(PageUrlEnum.CREATE_COURSE_PAGE_URL)