from automation.utils.logger import Logger


class RecoveryEngine:

    def __init__(self, page):

        self.page = page

    def recover_503(self):

        Logger.warning("503 Service Unavailable detected")

        for attempt in range(1, 4):

            Logger.info(f"Recovery Attempt {attempt}")

            self.page.reload(wait_until="domcontentloaded")

            self.page.wait_for_timeout(2000)

            title = self.page.title()

            if "503" not in title:

                Logger.success("Recovered Successfully")

                return True

        Logger.error("Recovery Failed")

        return False