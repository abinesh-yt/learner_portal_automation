import time

from automation.utils.logger import Logger


class Retry:

    @staticmethod
    def execute(
        function,
        retries=3,
        delay=2
    ):

        last_error = None

        for attempt in range(1, retries + 1):

            try:

                Logger.info(
                    f"Attempt {attempt}/{retries}"
                )

                return function()

            except Exception as e:

                Logger.warning(str(e))

                last_error = e

                time.sleep(delay)

        raise last_error