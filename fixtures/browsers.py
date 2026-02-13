import allure
from playwright.sync_api import Page, Playwright
import pytest
from _pytest.fixtures import SubRequest

from pages.authentication.registration_page import RegistrationPage


@pytest.fixture
def chromium_page(request: SubRequest, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context.new_page()

    trace_path = f'./tracing/{request.node.name}.zip'

    if request.node.rep_call.failed:
        context.tracing.stop(path=trace_path)
        allure.attach.file(source=trace_path, name='trace', extension='zip')
    elif request.node.rep_call.passed:
        context.tracing.stop()

    browser.close()


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
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield context.new_page()

    trace_path = f'./tracing/{request.node.name}.zip'

    if request.node.rep_call.failed:
        context.tracing.stop(path=trace_path)
        allure.attach.file(source=trace_path, name='trace', extension='zip')
    elif request.node.rep_call.passed:
        context.tracing.stop()

    browser.close()
