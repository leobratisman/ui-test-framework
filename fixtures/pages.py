import pytest
from playwright.sync_api import Page

from pages.login.login_page import LoginPage
from pages.dashboard.dashboard_page import DashboardPage
from pages.registration.registration_page import RegistrationPage
from pages.courses.courses_page import CoursesPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.fixture(scope="function")
def login_page(clean_page: Page) -> LoginPage:
    return LoginPage(page=clean_page)

@pytest.fixture(scope="function")
def login_page_with_state(authenticated_page: Page) -> LoginPage:
    return LoginPage(page=authenticated_page)


@pytest.fixture(scope="function")
def registration_page(clean_page: Page) -> RegistrationPage:
    return RegistrationPage(page=clean_page)


@pytest.fixture(scope="function")
def dashboard_page(clean_page: Page) -> DashboardPage:
    return DashboardPage(page=clean_page)

@pytest.fixture(scope="function")
def dashboard_page_with_state(authenticated_page: Page) -> DashboardPage:
    return DashboardPage(page=authenticated_page)


@pytest.fixture(scope="function")
def courses_page(authenticated_page: Page) -> CoursesPage:
    return CoursesPage(page=authenticated_page)


@pytest.fixture(scope="function")
def create_course_page(authenticated_page: Page) -> CreateCoursePage:
    return CreateCoursePage(page=authenticated_page)