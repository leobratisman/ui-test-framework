import pytest
import allure

from pages import LoginPage, DashboardPage, RegistrationPage
from enums import PageUrlEnum
from config import settings
from utils.allure import AllureTag, Severity, AllureEpic, AllureFeature, AllureStory


@allure.tag(AllureTag.AUTH, AllureTag.REGRESS)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHORIZATION)
@allure.story(AllureStory.AUTHENTICATION)
@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.auth
class TestLogin:
    @allure.severity(Severity.CRITICAL)
    @pytest.mark.parametrize("email, password", [
        ("user.name@gmail.com", "password"),
        ("user.name@gmail.com", " "),
        (" ", "password")
    ])
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str):
        allure.dynamic.title(f"User login with wrong email or password [{email} / {password}]")
        login_page.visit(url=PageUrlEnum.LOGIN_PAGE_URL)
        login_page.check_visible()
        login_page.login_form.fill(email=email, password=password)
        login_page.click_submit_button()
        login_page.check_visible_wrong_email_or_password_alert()

    @allure.title("User login with valid credentials")
    @allure.severity(Severity.BLOCKER)
    def test_successfull_authorization(
            self, 
            login_page_with_state: LoginPage, 
            dashboard_page_with_state: DashboardPage
        ):
        login_page_with_state.visit(url=PageUrlEnum.LOGIN_PAGE_URL)
        login_page_with_state.check_visible()
        login_page_with_state.login_form.fill(email=settings.TEST_USER.EMAIL, password=settings.TEST_USER.PASSWORD)
        login_page_with_state.click_submit_button()
        
        dashboard_page_with_state.check_url(url=PageUrlEnum.DASHBOARD_PAGE_URL)
        dashboard_page_with_state.sidebar.check_visible()
        dashboard_page_with_state.navbar.check_visible(username=settings.TEST_USER.USERNAME)

    @allure.tag(AllureTag.NAVIGATION)
    @allure.severity(Severity.CRITICAL)
    @allure.title("Navigate from login page to registration page")
    def test_navigation_from_login_to_registration(
            self, 
            login_page: LoginPage, 
            registration_page: RegistrationPage
        ):
        login_page.visit(url=PageUrlEnum.LOGIN_PAGE_URL)
        login_page.check_visible()
        login_page.click_registration_link()
        registration_page.check_url(url=PageUrlEnum.REGISTRATION_PAGE_URL)
        registration_page.check_visible()
