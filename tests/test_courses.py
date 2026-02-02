from playwright.sync_api import expect, Page
import pytest


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text('Courses')

    courses_icon_empty_block = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_icon_empty_block).to_be_visible()

    courses_subtitle_empty_block = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_subtitle_empty_block).to_be_visible()
    expect(courses_subtitle_empty_block).to_have_text('There is no results')

    cources_text_empty_block = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(cources_text_empty_block).to_be_visible()
    expect(cources_text_empty_block).to_have_text(
        'Results from the load test pipeline will be displayed here'
    )
