from playwright.sync_api import TimeoutError

from automation.utils.logger import Logger


class WaitEngine:

    @staticmethod
    def selector(page, selector, timeout=30000):

        Logger.info(f"Waiting for selector -> {selector}")

        page.locator(selector).wait_for(
            state="visible",
            timeout=timeout
        )

    @staticmethod
    def url_contains(page, text, timeout=30000):

        Logger.info(f"Waiting for URL -> {text}")

        page.wait_for_url(
            f"**{text}**",
            timeout=timeout
        )

    @staticmethod
    def page_title(page, text, timeout=30000):

        Logger.info(f"Waiting for title -> {text}")

        page.wait_for_function(
            f"document.title.includes('{text}')",
            timeout=timeout
        )

    @staticmethod
    def safe(page, selector, timeout=5000):

        try:

            page.locator(selector).wait_for(
                state="visible",
                timeout=timeout
            )

            return True

        except TimeoutError:

            return False