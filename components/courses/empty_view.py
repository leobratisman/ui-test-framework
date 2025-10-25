from playwright.sync_api import Page
import allure

from components.views.empty_view import EmptyView

class CoursesListEmptyView(EmptyView):
    def __init__(self, page: Page):
        super().__init__(page, identifier="courses-list")

    @allure.step("Checking courses empty view is visible")
    def check_visible(self):
        self.icon.check_visible()

        self.title.check_visible()
        self.title.check_have_text("There is no results")

        self.description.check_visible()
        self.description.check_have_text("Results from the load test pipeline will be displayed here")