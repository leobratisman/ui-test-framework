from playwright.sync_api import Page

from pages.base_page import BasePage
from components import Navbar, Sidebar, DashboardToolbar, WidgetsList

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.navbar = Navbar(self._page)
        self.sidebar = Sidebar(self._page)
        self.toolbar = DashboardToolbar(self._page)
        self.widgets_list = WidgetsList(page=self._page)
    
    def check_visible_widgets(self):
        self.widgets_list.check_visible()