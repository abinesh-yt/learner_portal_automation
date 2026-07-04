from automation.config.automation_config import AutomationConfig
from automation.worker.manager import WorkerManager

from dashboard.models import AutomationProfile


manager = WorkerManager()


def build_config():

    profile = AutomationProfile.objects.first()

    if profile is None:

        return None

    return AutomationConfig(

        website_url=profile.website_url,

        username=profile.username,

        password=profile.password,

        preferred_event=profile.preferred_event,

        preferred_slot=profile.preferred_slot,

        refresh_interval=profile.refresh_interval,

        retry_count=profile.retry_count,

        headless=profile.headless,

        automation_enabled=profile.automation_enabled,

    )


def start_automation():

    config = build_config()

    if config is None:

        return

    manager.start(config)


def stop_automation():

    manager.stop()


def automation_running():

    return manager.is_running()