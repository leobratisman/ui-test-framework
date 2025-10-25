from playwright.sync_api import Page
import allure

from components.base import BaseComponent
from elements import Input


class RegistrationForm(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def email_input(self) -> Input:
        return Input(self._page, "registration-form-email-input", "Email Input")
    
    @property
    def username_input(self) -> Input:
        return Input(self._page, "registration-form-username-input", "Username Input")
    
    @property
    def password_input(self) -> Input:
        return Input(self._page, "registration-form-password-input", "Password Input")
    
    @allure.step("Fill registration form")
    def fill(
        self,
        email: str,
        username: str,
        password: str
    ):
        self.email_input.fill(email)
        self.username_input.fill(username)
        self.password_input.fill(password)

    @allure.step("Checking registration form is visible")
    def check_visible(self):
        self.email_input.check_visible()
        self.username_input.check_visible()
        self.password_input.check_visible()