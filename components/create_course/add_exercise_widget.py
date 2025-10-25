from playwright.sync_api import Page
import allure

from components.base import BaseComponent
from components.create_course.add_exercise_toolbar import AddExerciseToolbar
from components.create_course.views.add_exercise_empty_view import AddExerciseEmptyView

from elements import Text, Button, Input


class AddExerciseWidget(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.toolbar = AddExerciseToolbar(page=self._page)
        self.add_exercise_empty_view = AddExerciseEmptyView(page=self._page)
    
    @property
    def exercise_box_toolbar_title(self) -> Text:
        return Text(self._page, "create-course-exercise-{index}-box-toolbar-subtitle-text", "Exercise toolbar title")
    
    @property
    def exercise_box_toolbar_delete_button(self) -> Button:
        return Button(
            page=self._page, 
            selector="create-course-exercise-{index}-box-toolbar-delete-exercise-button", 
            name="Exercise toolbar delete button"
        )
    
    @property
    def exercise_box_title_input(self) -> Input:
        return Input(self._page, "create-course-exercise-form-title-{index}-input", "Exercise title input")
    
    @property
    def exercise_box_description_input(self) -> Input:
        return Input(self._page, "create-course-exercise-form-description-{index}-input", "Exercise description input")

    @allure.step("Click delete exercise button")
    def click_delete_exercise(self, index: int = 0):
        self.exercise_box_toolbar_delete_button.click(index=index)

    @allure.step("Fill add exercise form")
    def fill_add_exercise_form(self, title: str, description: str, index: int = 0):
        self.exercise_box_title_input.fill(title, index=index)
        self.exercise_box_title_input.check_have_value(title, index=index)

        self.exercise_box_description_input.fill(description, index=index)
        self.exercise_box_description_input.check_have_value(description, index=index)

    @allure.step("Checking exercise info box is visible")
    def check_visible_exercise_box(self, index: int = 0):
        self.exercise_box_toolbar_title.check_visible(index=index)
        self.exercise_box_toolbar_title.check_have_text(f"#{index + 1} Exercise", index=index)

        self.exercise_box_toolbar_delete_button.check_visible(index=index)
        self.exercise_box_title_input.check_visible(index=index)
        self.exercise_box_description_input.check_visible(index=index)

