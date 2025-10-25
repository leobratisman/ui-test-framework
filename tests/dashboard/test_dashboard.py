import pytest
import allure

from pages import DashboardPage
from enums import PageUrlEnum

from config import settings
from utils.allure import AllureTag, AllureEpic, AllureFeature, AllureStory, Severity


@allure.tag(AllureTag.REGRESS, AllureTag.DASHBOARD)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.DASHBOARD)
@allure.story(AllureStory.DASHBOARD_VISIBILITY)
@pytest.mark.regress
@pytest.mark.smoke
@pytest.mark.dashboard
class TestDashboard:
    @allure.title("Dashboard displaying")
    @allure.severity(Severity.NORMAL)
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit(url=PageUrlEnum.DASHBOARD_PAGE_URL)
        dashboard_page_with_state.toolbar.check_visible()
        dashboard_page_with_state.check_visible_widgets()
        dashboard_page_with_state.sidebar.check_visible()
        dashboard_page_with_state.navbar.check_visible(username=settings.TEST_USER.USERNAME)