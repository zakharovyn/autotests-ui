from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from elements.image import Image
from elements.text import Text


class ChartViewComponent(BaseComponent):

    def __init__(self, page: Page, identifier: str, chart_type: str):
        super().__init__(page)

        self.title = Text(page, 'Title', f'{identifier}-widget-title-text')
        self.chart = Image(page, 'Chart', f'{identifier}-{chart_type}-chart')

    def check_visible(self, title: str):
        self.title.check_visible()
        self.title.check_have_text(title)

        self.chart.check_visible()
