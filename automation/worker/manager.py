from automation.worker.worker import AutomationWorker


class WorkerManager:

    def __init__(self):

        self.worker = None

    def start(self, config):

        if self.is_running():

            return

        self.worker = AutomationWorker(config)

        self.worker.start()

    def stop(self):

        if self.is_running():

            self.worker.terminate()

            self.worker.join()

            self.worker = None

    def is_running(self):

        return self.worker is not None and self.worker.is_alive()