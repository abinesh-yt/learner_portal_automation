from automation.models.event import Event
from automation.pages.base_page import BasePage

from automation.selectors.booking_selectors import BookingSelectors

from automation.utils.logger import Logger


class BookingPage(BasePage):

    def get_events(self):

        cards = self.page.locator(
            BookingSelectors.EVENT_CARD
        )

        Logger.info(
            f"Found {cards.count()} Event Cards"
        )

        events = []

        for i in range(cards.count()):

            try:

                card = cards.nth(i)

                # -----------------------
                # Title
                # -----------------------

                title = ""

                title_locator = card.locator(
                    BookingSelectors.TITLE
                )

                if title_locator.count():

                    title = title_locator.first.inner_text().strip()

                else:

                    Logger.warning(
                        f"Card {i+1} has no title. Skipping."
                    )

                    continue

                # -----------------------
                # Status
                # -----------------------

                status = ""

                badge = card.locator(
                    BookingSelectors.STATUS
                )

                if badge.count():

                    status = badge.first.inner_text().strip()

                # -----------------------
                # Small Text
                # -----------------------

                date_time = ""

                venue = ""

                booking_window = ""

                capacity = ""

                smalls = card.locator(
                    BookingSelectors.SMALL_TEXT
                )

                for j in range(smalls.count()):

                    text = smalls.nth(j).inner_text().strip()

                    if not date_time:

                        date_time = text

                    elif text.startswith("Venue"):

                        venue = text

                    elif text.startswith("Booking Window"):

                        booking_window = text

                    elif text.startswith("Capacity"):

                        capacity = text

                # -----------------------
                # Buttons
                # -----------------------

                can_book = False

                if card.locator(
                    BookingSelectors.BOOK_BUTTON
                ).count():

                    can_book = True

                has_view_more = False

                if card.locator(
                    BookingSelectors.VIEW_MORE
                ).count():

                    has_view_more = True

                event = Event(

                    title=title,

                    date_time=date_time,

                    venue=venue,

                    booking_window=booking_window,

                    capacity=capacity,

                    status=status,

                )

                # Temporary properties
                event.can_book = can_book
                event.has_view_more = has_view_more

                events.append(event)

            except Exception as e:

                Logger.warning(
                    f"Skipping Card {i+1}: {e}"
                )

                continue

        Logger.success(
            f"{len(events)} Events Parsed Successfully"
        )

        return events