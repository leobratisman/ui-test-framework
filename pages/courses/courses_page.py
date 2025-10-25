from playwright.sync_api import Page

from pages.base_page import BasePage
from components import CourseWidget, Navbar, Sidebar, CoursesToolbar, CoursesListEmptyView


class CoursesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.navbar = Navbar(self._page)
        self.sidebar = Sidebar(self._page)
        self.toolbar = CoursesToolbar(self._page)
        self.course_widget = CourseWidget(self._page)
        self.courses_list_empty_view = CoursesListEmptyView(self._page)


    
    
