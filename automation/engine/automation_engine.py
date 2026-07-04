from automation.browser.browser_manager import BrowserManager
from automation.workflows.login_workflow import LoginWorkflow
from automation.workflows.booking_workflow import BookingWorkflow
from automation.decision.decision_engine import DecisionEngine
from automation.state.states import AutomationState
from automation.utils.logger import Logger
from automation.runtime.runtime import update

class AutomationEngine:

    def __init__(self):

        self.browser = None
        self.page = None
        self.state = AutomationState.START

    def set_state(self, state):

        self.state = state

        Logger.info(f"STATE -> {state.value}")

    def start(self, config):

        self.browser = BrowserManager(
            headless=config.headless
        )

        try:

            self.set_state(
                AutomationState.START
            )

            self.page = self.browser.start()

            update(

                running=True,

                browser_connected=True,

                current_state="LOGIN"

            )

            self.set_state(
                AutomationState.LOGIN
            )

            LoginWorkflow(
                self.page
            ).execute(

                website=config.website_url,

                username=config.username,

                password=config.password,

            )
            update(

    logged_in=True,

    current_state="BOOKINGS"

)

            self.set_state(
                AutomationState.OPEN_BOOKINGS
            )

            events = BookingWorkflow(
                self.page
            ).execute()

            self.set_state(
                AutomationState.READ_EVENTS
            )

            Logger.success(
                f"{len(events)} Events Loaded"
            )

            self.set_state(
                AutomationState.DECISION
            )

            decision = DecisionEngine(
                config
            )

            selected = decision.choose_event(
                events
            )
            if selected:

                update(

                    last_event=selected.title,

                    last_status=selected.status,

                    current_state="MATCH_FOUND"

                )

            else:

                update(

                    current_state="WAITING"

                )

            if selected is None:

                self.set_state(
                    AutomationState.WAITING
                )

                Logger.warning(
                    "No Matching Event"
                )

                return

            Logger.success(
                f"Selected Event : {selected.title}"
            )

            Logger.info(
                f"Status : {selected.status}"
            )

            Logger.info(
                f"Venue : {selected.venue}"
            )

            Logger.info(
                f"Capacity : {selected.capacity}"
            )

            if selected.can_book:

                Logger.success(
                    "Booking Button Available"
                )

            else:

                Logger.warning(
                    "Booking Closed"
                )

            self.set_state(
                AutomationState.SUCCESS
            )

        except Exception as e:

            self.set_state(
                AutomationState.FAILED
            )

            Logger.error(str(e))

        finally:

            self.set_state(
                AutomationState.END
            )

            update(

            running=False,

            browser_connected=False,

            logged_in=False,

            current_state="STOPPED"

        )

        self.browser.close()