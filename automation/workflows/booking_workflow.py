from automation.pages.booking_page import BookingPage

from automation.workflows.navigation_workflow import NavigationWorkflow

from automation.utils.logger import Logger


class BookingWorkflow:

    def __init__(self, page):

        self.navigation = NavigationWorkflow(page)

        self.booking = BookingPage(page)

    def execute(self):

        self.navigation.open_bookings()

        Logger.info("Extracting Events")

        return self.booking.get_events()