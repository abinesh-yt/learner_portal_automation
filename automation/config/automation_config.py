from dataclasses import dataclass


@dataclass
class AutomationConfig:

    website_url: str

    username: str

    password: str

    preferred_event: str

    preferred_slot: str

    refresh_interval: int

    retry_count: int

    headless: bool

    automation_enabled: bool