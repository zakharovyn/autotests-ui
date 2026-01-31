from playwright.sync_api import sync_playwright, Request, Response
from http import HTTPStatus


def log_request(request: Request):
    print(f'Request: {request.url}')


def log_response(response: Response):
    print(f'Response: {response.url}, {response.status} {HTTPStatus(response.status).phrase}')


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.on(event='request', f=log_request)
    page.on(event='response', f=log_response)

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    page.wait_for_timeout(1000)
