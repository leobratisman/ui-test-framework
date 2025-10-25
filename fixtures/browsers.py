import pytest
import allure
from _pytest.fixtures import SubRequest
from typing import Generator
from playwright.sync_api import Page, Playwright, Browser

from pages.registration.registration_page import RegistrationPage
from utils.playwright.mock import mock_static_resources
from config import settings
from enums import PageUrlEnum


@pytest.fixture(scope="session", params=settings.BROWSERS_LIST)
def browser(request: SubRequest, playwright: Playwright) -> Generator[Browser]:
    browser_type = request.param
    browser = playwright[browser_type].launch(headless=settings.HEADLESS)
    yield browser
    browser.close()

@pytest.fixture(scope="session")
def auth_state_file(browser: Browser) -> str:
    context = browser.new_context()
    page = context.new_page()
    
    registration_page = RegistrationPage(page)
    registration_page.visit(url=PageUrlEnum.REGISTRATION_PAGE_URL)
    registration_page.registration_form.fill(
        email=settings.TEST_USER.EMAIL,
        username=settings.TEST_USER.USERNAME,
        password=settings.TEST_USER.PASSWORD
    )
    registration_page.click_form_submit_button()
    registration_page.is_registration_successfull()

    context.storage_state(path=settings.BROWSER_STATE_LOCATION)
    context.close()

    return settings.BROWSER_STATE_LOCATION

def initialize_page(
    request: SubRequest,
    browser: Browser,
    browser_state_file = None
):
    if browser_state_file:
        context = browser.new_context(storage_state=browser_state_file)
    else:
        context = browser.new_context()

    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    mock_static_resources(page)

    yield page
    context.tracing.stop(path=f"{settings.TRACING_DIR}/{request.node.name}.zip")
    allure.attach.file(source=f"{settings.TRACING_DIR}/{request.node.name}.zip", name="trace", extension="zip")
    context.close()

@pytest.fixture(scope="function")
def clean_page(request: SubRequest, browser: Browser) -> Generator[Page]:
    yield from initialize_page(
        request=request,
        browser=browser
    )

@pytest.fixture(scope="function")
def authenticated_page(request: SubRequest, browser: Browser, auth_state_file: str) -> Generator[Page]:
    yield from initialize_page(
        request=request,
        browser=browser,
        browser_state_file=auth_state_file
    )
