from automation.pages.base_page import BasePage
from automation.utils.logger import Logger


class DashboardPage(BasePage):

    LOGGED_IN = "text=Logged in as:"
    BOOKINGS = "a[href='/academicevents/event-booking/']"

    def verify_login(self):

        Logger.info("Verifying Login")

        self.wait_visible(self.LOGGED_IN)

        Logger.success("Login Successful")

    def open_bookings(self):

        Logger.info("Opening Booking Page")

        self.click(self.BOOKINGS)

        Logger.success("Booking Page Opened")