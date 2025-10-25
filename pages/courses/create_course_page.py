from playwright.sync_api import Locator, Page, expect

from pages.base_page import BasePage
from components import (
    UploadImageWidget, 
    CourseDataForm, 
    AddExerciseWidget,
    Navbar,
    Sidebar,
    CreateCourseToolbar
)


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.navbar = Navbar(self._page)
        self.sidebar = Sidebar(self._page)
        self.toolbar = CreateCourseToolbar(self._page)

        self.upload_image_widget = UploadImageWidget(self._page)
        self.course_data_form = CourseDataForm(self._page)
        self.add_exercise_widget = AddExerciseWidget(self._page)