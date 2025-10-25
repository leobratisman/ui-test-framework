from playwright.sync_api import expect

from components.views.empty_view import EmptyView

class AddExerciseEmptyView(EmptyView):
    def __init__(self, page):
        super().__init__(page, identifier="create-course-exercises")

    def check_visible(self):
        self.icon.check_visible()

        self.title.check_visible()
        self.title.check_have_text("There is no exercises")

        self.description.check_visible()
        self.description.check_have_text('Click on "Create exercise" button to create new exercise')