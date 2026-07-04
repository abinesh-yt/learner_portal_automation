from dataclasses import dataclass


@dataclass
class Event:

    title: str

    date_time: str

    venue: str

    booking_window: str

    capacity: str

    status: str

    can_book: bool = False

    has_view_more: bool = False