import pytest
import allure

from pages import RegistrationPage, DashboardPage
from config import settings
from enums import PageUrlEnum
from utils.allure import AllureTag, AllureStory, AllureEpic, AllureFeature, Severity


@allure.tag(AllureTag.REGRESS, AllureTag.AUTH)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHORIZATION)
@allure.story(AllureStory.REGISTRATION)
@pytest.mark.smoke
@pytest.mark.regress
@pytest.mark.registration
class TestRegistration:
    @allure.title("Successfull registration")
    @allure.severity(Severity.BLOCKER)
    def test_successfull_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit(url=PageUrlEnum.REGISTRATION_PAGE_URL)
        registration_page.check_visible()
        registration_page.registration_form.fill(
            email=settings.TEST_USER.EMAIL,
            username=settings.TEST_USER.USERNAME,
            password=settings.TEST_USER.PASSWORD
        )
        registration_page.click_form_submit_button()
        registration_page.check_url(url=PageUrlEnum.DASHBOARD_PAGE_URL)
        dashboard_page.toolbar.check_visible()
