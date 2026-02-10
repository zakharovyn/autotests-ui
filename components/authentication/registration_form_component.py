from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.input import Input


class RegistrationFormComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, "Email input", "registration-form-email-input")
        self.username_input = Input(page, "Username input", "registration-form-username-input")
        self.password_input = Input(page, "Password input", "registration-form-password-input")

    def fill(self, email: str, username: str, password: str):
        self.email_input.fill(value=email)
        self.email_input.check_have_value(value=email)

        self.username_input.fill(value=username)
        self.username_input.check_have_value(value=username)

        self.password_input.fill(value=password)
        self.password_input.check_have_value(value=password)

    def check_visible(self, email: str, username: str, password: str):
        self.email_input.check_visible()
        self.email_input.check_have_value(value=email)

        self.username_input.check_visible()
        self.username_input.check_have_value(value=username)

        self.password_input.check_visible()
        self.password_input.check_have_value(value=password)
