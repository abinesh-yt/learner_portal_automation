from multiprocessing import Process
import time

from automation.engine.automation_engine import AutomationEngine
from automation.utils.logger import Logger


class AutomationWorker(Process):

    def __init__(self, config):

        super().__init__()

        self.config = config

    def run(self):

        Logger.success("Automation Worker Started")

        while True:

            try:

                engine = AutomationEngine()

                engine.start(self.config)

            except Exception as e:

                Logger.error(str(e))

            Logger.info(
                f"Sleeping {self.config.refresh_interval} seconds..."
            )

            time.sleep(self.config.refresh_interval)