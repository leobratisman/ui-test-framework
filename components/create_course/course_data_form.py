from playwright.sync_api import Page
import allure

from dto.course_dto import CreateCourseDataDTO
from components.base import BaseComponent
from elements import Input, Textarea


class CourseDataForm(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def title_input(self) -> Input:
        return Input(self._page, "create-course-form-title-input", "Title input")
    
    @property
    def estimated_time_input(self) -> Input:
        return Input(self._page, "create-course-form-estimated-time-input", "Estimated time input")
    
    @property
    def description_input(self) -> Textarea:
        return Textarea(self._page, "create-course-form-description-input", "Description input")
    
    @property
    def max_score_input(self) -> Input:
        return Input(self._page, "create-course-form-max-score-input", "Max score input")
    
    @property
    def min_score_input(self) -> Input:
        return Input(self._page, "create-course-form-min-score-input", "Min score input")
    
    @allure.step("Fill create course form")
    def fill_create_course_form(self, data: CreateCourseDataDTO):
        self.title_input.fill(data.title)
        self.title_input.check_have_value(data.title)

        self.estimated_time_input.fill(data.estimated_time)
        self.estimated_time_input.check_have_value(data.estimated_time)

        self.description_input.fill(data.description)
        self.description_input.check_have_value(data.description)

        self.max_score_input.fill(str(data.max_score))
        self.max_score_input.check_have_value(str(data.max_score))

        self.min_score_input.fill(str(data.min_score))
        self.min_score_input.check_have_value(str(data.min_score))