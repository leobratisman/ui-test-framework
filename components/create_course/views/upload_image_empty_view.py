from playwright.sync_api import Page
import allure

from components.views.empty_view import EmptyView

class UploadImageEmptyView(EmptyView):
    def __init__(self, page):
        super().__init__(page, identifier="create-course-preview")

    @allure.step("Checking upload course empty preview is visible")
    def check_visible(self):
        self.icon.check_visible()

        self.title.check_visible()
        self.title.check_have_text("No image selected")

        self.description.check_visible()
        self.description.check_have_text("Preview of selected image will be displayed here")