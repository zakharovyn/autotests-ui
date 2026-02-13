from playwright.sync_api import Page, Playwright
import pytest
from _pytest.fixtures import SubRequest

from pages.authentication.registration_page import RegistrationPage
from tools.playwtight.pages import initialize_playwright_page


@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    yield from initialize_playwright_page(
        playwright=playwright,
        request=request,
        test_name=request.node.name,
    )


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page)
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(email='user@gmail.com', username='username', password='password')
    registration_page.click_registration_button()

    context.storage_state(path='browser-state.json')
    browser.close()


@pytest.fixture
def chromium_page_with_state(
        request: SubRequest,
        initialize_browser_state,
        playwright: Playwright
) -> Page:
    yield from initialize_playwright_page(
        playwright=playwright,
        test_name=request.node.name,
        request=request,
        storage_state='browser-state.json'
    )
