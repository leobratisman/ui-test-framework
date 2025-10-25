from playwright.sync_api import Page
import allure

from pages.base_page import BasePage
from components import LoginForm
from elements import Button, Text, Link


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.login_form = LoginForm(self._page)

    @property
    def title(self) -> Text:
        return Text(self._page, "authentication-ui-course-title-text", "Login page title")
    
    @property
    def form_submit_button(self) -> Button:
        return Button(self._page, "login-page-login-button", "Submit button")
    
    @property
    def link_to_registration_page(self) -> Link:
        return Link(self._page, "login-page-registration-link", "Link to registration")
        
    @property
    def wrong_email_or_password_alert(self) -> Text:
        return Text(self._page, "login-page-wrong-email-or-password-alert", "Wrong email or password alert")

    @allure.step("Click login submit button")
    def click_submit_button(self):
        self.form_submit_button.click()

    @allure.step('Click "Registration" link')
    def click_registration_link(self):
        self.link_to_registration_page.click()

    @allure.step('Checking wrong email or password alert is visible')
    def check_visible_wrong_email_or_password_alert(self):
        self.wrong_email_or_password_alert.check_visible()
        self.wrong_email_or_password_alert.check_have_text("Wrong email or password")

    @allure.step('Checking login page is visible')
    def check_visible(self):
        self.login_form.check_visible()
        self.title.check_visible()
        self.title.check_have_text("UI Course")

        self.form_submit_button.check_visible()
        self.link_to_registration_page.check_visible()
        self.link_to_registration_page.check_have_text("Registration")
