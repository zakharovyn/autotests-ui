import allure
from playwright.sync_api import Playwright, Page
from _pytest.fixtures import SubRequest

from config import settings, Browser


def initialize_playwright_page(
        playwright: Playwright,
        test_name: str,
        request: SubRequest,
        browser_type: Browser,
        storage_state: str | None = None
) -> Page:
    browser = playwright[browser_type].launch(headless=settings.headless)
    # context = browser.new_context(base_url=settings.get_base_url(), storage_state=storage_state, record_video_dir=settings.videos_dir)
    context = browser.new_context(
        base_url=settings.get_base_url(),
        storage_state=storage_state
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    yield page

    trace_path = settings.tracing_dir.joinpath(f'{test_name}.zip')

    if request.node.rep_call.failed:
        context.tracing.stop(path=trace_path)
        allure.attach.file(source=trace_path, name='trace', extension='zip')
    elif request.node.rep_call.passed:
        context.tracing.stop()

    # allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)
    browser.close()


# def initialize_playwright_page(
#         playwright: Playwright,
#         test_name: str,
#         request: SubRequest,
#         storage_state: str | None = None
# ) -> Page:
#     browser = playwright.chromium.launch(headless=settings.headless)
#     # context = browser.new_context(base_url=settings.get_base_url(), storage_state=storage_state, record_video_dir=settings.videos_dir)
#     context = browser.new_context(
#         base_url=settings.get_base_url(),
#         storage_state=storage_state
#     )
#     context.tracing.start(screenshots=True, snapshots=True, sources=True)
#     page = context.new_page()
#
#     yield page
#
#     trace_path = settings.tracing_dir.joinpath(f'{test_name}.zip')
#
#     if request.node.rep_call.failed:
#         context.tracing.stop(path=trace_path)
#         allure.attach.file(source=trace_path, name='trace', extension='zip')
#     elif request.node.rep_call.passed:
#         context.tracing.stop()
#
#     # allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)
#     browser.close()



