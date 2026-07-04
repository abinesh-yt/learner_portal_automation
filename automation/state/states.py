from enum import Enum


class AutomationState(Enum):

    START = "START"

    LOGIN = "LOGIN"

    VERIFY_LOGIN = "VERIFY_LOGIN"

    OPEN_BOOKINGS = "OPEN_BOOKINGS"

    READ_EVENTS = "READ_EVENTS"

    DECISION = "DECISION"

    BOOK = "BOOK"

    SUCCESS = "SUCCESS"

    FAILED = "FAILED"

    END = "END"