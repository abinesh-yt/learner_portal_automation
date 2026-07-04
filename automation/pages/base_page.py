from playwright.sync_api import Page

from automation.utils.wait_engine import WaitEngine


class BasePage:

    def __init__(self, page: Page):

        self.page = page

    def open(self, url):

        self.page.goto(
            url,
            wait_until="domcontentloaded"
        )

    def click(self, selector):

        WaitEngine.selector(
            self.page,
            selector
        )

        self.page.locator(
            selector
        ).click()

    def fill(self, selector, value):

        WaitEngine.selector(
            self.page,
            selector
        )

        self.page.locator(
            selector
        ).fill(value)

    def exists(self, selector):

        return WaitEngine.safe(
            self.page,
            selector
        )

    def text(self, selector):

        return self.page.locator(
            selector
        ).inner_text()