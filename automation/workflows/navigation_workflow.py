from automation.utils.logger import Logger

from automation.selectors.booking_selectors import BookingSelectors

from automation.recovery.recovery_engine import RecoveryEngine


class NavigationWorkflow:

    def __init__(self, page):

        self.page = page

        self.recovery = RecoveryEngine(page)

    def open_bookings(self):

        Logger.info("Navigating To Booking Page")

        self.page.locator(

            BookingSelectors.BOOKINGS_MENU

        ).click()

        self.page.wait_for_timeout(2000)

        title = self.page.title()

        if "503" in title:

            if not self.recovery.recover_503():

                raise Exception(

                    "Booking Page Unavailable"

                )

        if "event-booking" not in self.page.url:

            raise Exception(

                "Navigation Failed"

            )

        Logger.success(

            "Booking Page Ready"

        )