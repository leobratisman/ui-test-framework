from playwright.sync_api import Page
import allure

from components.base import BaseComponent
from elements import Input


class LoginForm(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def email_input(self) -> Input:
        return Input(self._page, "login-form-email-input", "Email input")
    
    @property
    def password_input(self) -> Input:
        return Input(self._page, "login-form-password-input", "Password input")
    
    @allure.step("Fill login form")
    def fill(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)

    @allure.step("Checking login form is visible")
    def check_visible(self):
        self.email_input.check_visible()
        self.password_input.check_visible()