from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.icon import Icon
from elements.text import Text


class EmptyViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.icon = Icon(page, '{identifier}-empty-view-icon', 'Emtpy view icon')
        self.title = Text(page, '{identifier}-empty-view-title-text', 'Emtpy view title')
        self.description = Text(page, '{identifier}-empty-view-description-text', 'Emtpy view title')

    def check_visible(self, title: str, description: str, identifier: str):
        self.icon.check_visible(identifier=identifier)
        self.title.check_visible(identifier=identifier)
        self.title.check_text(title, identifier=identifier)
        self.description.check_visible(identifier=identifier)
        self.description.check_text(description, identifier=identifier)
