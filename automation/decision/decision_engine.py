from automation.utils.logger import Logger


class DecisionEngine:

    def __init__(self, config):

        self.config = config

    def choose_event(self, events):

        Logger.info("Searching Preferred Event")

        for event in events:

            if self.config.preferred_event.lower() not in event.title.lower():

                continue

            if self.config.preferred_slot:

                if self.config.preferred_slot.lower() not in event.date_time.lower():

                    continue

            Logger.success(
                f"Selected {event.title}"
            )

            return event

        Logger.warning("No Matching Event")

        return None