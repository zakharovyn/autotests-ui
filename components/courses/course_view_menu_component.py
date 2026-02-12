import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.button import Button


class CourseViewMenuComponent(BaseComponent):

    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = Button(page, 'Menu', 'course-view-menu-button')
        self.edit_menu_button = Button(page, 'Edit', 'course-view-edit-menu-item')
        self.delete_menu_button = Button(page, 'Delete', 'course-view-delete-menu-item')

    @allure.step('Open course menu at index "{index}" and click edit')
    def click_edit(self, index: int = 0):
        self.menu_button.click(nth=index)

        self.edit_menu_button.check_visible(nth=index)
        self.edit_menu_button.click(nth=index)

    @allure.step('Open course menu at index "{index}" and click delete')
    def click_delete(self, index: int = 0):
        self.delete_menu_button.click(nth=index)

        self.delete_menu_button.check_visible(nth=index)
        self.delete_menu_button.click(nth=index)
