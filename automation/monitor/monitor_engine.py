from automation.utils.logger import Logger


class MonitorEngine:

    def __init__(self, page, booking_page):

        self.page = page
        self.booking_page = booking_page

    def refresh(self):

        Logger.info("Refreshing Booking Page")

        self.page.reload(
            wait_until="domcontentloaded"
        )

        self.page.wait_for_timeout(2000)

    def read_events(self):

        return self.booking_page.get_events()