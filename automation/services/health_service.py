from automation.runtime.runtime import runtime


class HealthService:

    @staticmethod
    def healthy():

        return (

            runtime.running and

            runtime.browser_connected

        )