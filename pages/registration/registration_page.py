from playwright.sync_api import Page
import allure

from pages.base_page import BasePage
from components import RegistrationForm
from elements import Button, Text, Link

from enums import PageUrlEnum


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.registration_form = RegistrationForm(self._page)

    @property
    def title(self) -> Text:
        return Text(self._page, "authentication-ui-course-title-text", "Registration page title")
    
    @property
    def form_submit_button(self) -> Button:
        return Button(self._page, "registration-page-registration-button", "Submit button")
    
    @property
    def link_to_login_page(self) -> Link:
        return Link(self._page, "registration-page-login-link", "Link to login")

    @allure.step("Click registration submit button")
    def click_form_submit_button(self):
        self.form_submit_button.click()

    @allure.step('Click "Login" link')
    def click_login_link(self):
        self.link_to_login_page.click()

    @allure.step('Checking registration page is visible')
    def check_visible(self):
        self.registration_form.check_visible()
        self.title.check_visible()
        self.title.check_have_text("UI Course")

        self.form_submit_button.check_visible()
        self.link_to_login_page.check_visible()
        self.link_to_login_page.check_have_text("Login")

    @allure.step('Checking registration is successfull')
    def is_registration_successfull(self):
        self.wait_for_page_loaded()
        self.check_url(PageUrlEnum.DASHBOARD_PAGE_URL)
