from playwright.sync_api import Page
import allure

from components.base import BaseComponent
from components.create_course.course_image_preview import CourseImagePreview
from elements import Icon, Text, Button, FileInput

from config import settings


class UploadImageWidget(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.image_preview = CourseImagePreview(self._page)

    @property
    def image_upload_icon(self) -> Icon:
        return Icon(self._page, "create-course-preview-image-upload-widget-info-icon", "Image upload icon")
    
    @property
    def image_upload_title(self) -> Text:
        return Text(self._page, "create-course-preview-image-upload-widget-info-title-text", "Image upload title")
    
    @property
    def image_upload_description(self) -> Text:
        return Text(self._page, "create-course-preview-image-upload-widget-info-description-text", "Image upload description")
    
    @property
    def image_upload_button(self) -> Button:
        return Button(self._page, "create-course-preview-image-upload-widget-upload-button", "Image upload button")
    
    @property
    def image_remove_button(self) -> Button:
        return Button(self._page, "create-course-preview-image-upload-widget-remove-button", "Image remove button")
    
    @property
    def image_upload_input(self) -> FileInput:
        return FileInput(self._page, "create-course-preview-image-upload-widget-input", "Image upload input")
    
    @allure.step("Checking upload image widget is visible")
    def check_visible(self, is_image_uploaded: bool):
        if not is_image_uploaded:
            self.image_preview.upload_image_empty_view.check_visible()
        else:
            self.image_preview.check_visible_preview_image()
            self.image_remove_button.check_visible()

        self.image_upload_icon.check_visible()
        self.image_upload_title.check_visible()
        self.image_upload_title.check_have_text('Tap on "Upload image" button to select file')

        self.image_upload_description.check_visible()
        self.image_upload_description.check_have_text("Recommended file size 540X300")

        self.image_upload_button.check_visible()

    @allure.step("Click image upload button")
    def click_image_upload_button(self):
        self.image_upload_button.click()

    @allure.step("Click image remove button")
    def click_image_remove_button(self):
        self.image_remove_button.check_visible()
        self.image_remove_button.check_enabled()
        self.image_remove_button.click()

    def upload_preview_image(self, file: str):
        with allure.step(f"Uploading course preview from {file}"):
            self.image_upload_input.upload(file_path=f"{settings.TEST_DATA.IMAGE_PNG_FILE}")
