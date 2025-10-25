from playwright.sync_api import Page
import allure

from components.base import BaseComponent
from components.courses.course_widget_menu import CourseWidgetMenu
from dto.course_dto import CheckCourseWidgetDTO

from elements import Text, Button, Image, Icon


class CourseWidget(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.menu = CourseWidgetMenu(self._page)

    @property
    def course_title(self) -> Text:
        return Text(self._page, "course-widget-title-text", "Course title")
    
    @property
    def course_menu_button(self) -> Button:
        return Button(self._page, "course-view-menu-button", "Course menu button")
    
    @property
    def course_preview_image(self) -> Image:
        return Image(self._page, "course-preview-image", "Course preview image")
    
    @property
    def course_max_score_icon(self) -> Icon:
        return Icon(self._page, "course-max-score-info-row-view-icon", "Course max score icon")

    @property
    def course_max_score_text(self) -> Text:
        return Text(self._page, "course-max-score-info-row-view-text", "Course max score text")

    @property
    def course_min_score_icon(self) -> Icon:
        return Icon(self._page, "course-min-score-info-row-view-icon", "Course min score icon")

    @property
    def course_min_score_text(self) -> Text:
        return Text(self._page, "course-min-score-info-row-view-text", "Course min score text")

    @property
    def course_estimated_time_icon(self) -> Icon:
        return Icon(self._page, "course-estimated-time-info-row-view-icon", "Course estimated time icon")

    @property
    def course_estimated_time_text(self) -> Text:
        return Text(self._page, "course-estimated-time-info-row-view-text", "Course estimated time text")
    
    def click_course_menu_edit_item(self, index: int = 0):
        with allure.step(f'Click course at index {index} menu edit button'):
            self.course_menu_button.click(nth=index)
            self.menu.click_edit_item(index)

    def click_course_menu_delete_item(self, index: int = 0):
        with allure.step(f'Click course at index {index} menu delete button'):
            self.course_menu_button.nth(index).click()
            self.menu.click_edit_item(index)
    
    def check_visible_course_widget(self, course_data: CheckCourseWidgetDTO):
        with allure.step(f"Checking course widget at index {course_data.index} is visible"):
            self.course_preview_image.check_visible(nth=course_data.index)

            self.course_title.check_visible(nth=course_data.index)
            self.course_title.check_have_text(course_data.title, nth=course_data.index)

            self.course_max_score_text.check_visible(nth=course_data.index)
            self.course_max_score_text.check_have_text(f"Max score: {course_data.max_score}", nth=course_data.index)

            self.course_min_score_text.check_visible(nth=course_data.index)
            self.course_min_score_text.check_have_text(f"Min score: {course_data.min_score}", nth=course_data.index)

            self.course_estimated_time_text.check_visible(nth=course_data.index)
            self.course_estimated_time_text.check_have_text(
                f"Estimated time: {course_data.estimated_time}", nth=course_data.index
            )

    