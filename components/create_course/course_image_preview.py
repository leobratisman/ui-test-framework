from playwright.sync_api import Page
import allure

from components.base import BaseComponent
from components.create_course.views.upload_image_empty_view import UploadImageEmptyView
from elements import Image


class CourseImagePreview(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.upload_image_empty_view = UploadImageEmptyView(page=self._page)

    @property
    def preview_image(self) -> Image:
        return Image(self._page, "create-course-preview-image-upload-widget-preview-image", "Course preview image")

    @allure.step("Checking course preview image is visible")
    def check_visible_preview_image(self):
        self.preview_image.check_visible()