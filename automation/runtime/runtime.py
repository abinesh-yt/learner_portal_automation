from dataclasses import dataclass
from datetime import datetime


@dataclass
class RuntimeState:

    running: bool = False

    browser_connected: bool = False

    logged_in: bool = False

    current_state: str = "IDLE"

    last_event: str = ""

    last_status: str = ""

    last_check: str = ""

    worker_pid: int | None = None


runtime = RuntimeState()


def update(**kwargs):

    for key, value in kwargs.items():

        setattr(runtime, key, value)

    runtime.last_check = datetime.now().strftime(
        "%H:%M:%S"
    )