from automation.worker.manager import WorkerManager


class AutomationService:

    def __init__(self):
        self.manager = WorkerManager()

    def start(self, config):

        if self.manager.is_running():
            return False

        self.manager.start(config)

        return True

    def stop(self):

        self.manager.stop()

    def restart(self, config):

        self.stop()
        self.start(config)

    def running(self):

        return self.manager.is_running()