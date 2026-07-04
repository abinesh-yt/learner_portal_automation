from automation.runtime.runtime import runtime


class StatusService:

    @staticmethod
    def get():

        return {

            "running": runtime.running,

            "browser": runtime.browser_connected,

            "logged_in": runtime.logged_in,

            "state": runtime.current_state,

            "last_event": runtime.last_event,

            "last_status": runtime.last_status,

            "last_check": runtime.last_check,

        }