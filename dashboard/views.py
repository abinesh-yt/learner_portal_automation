from threading import Thread

from django.shortcuts import redirect, render

from .models import AutomationProfile
from .services import start_automation


def home(request):

    profile = AutomationProfile.objects.first()

    if request.method == "POST":

        if "save" in request.POST:

            if profile is None:
                profile = AutomationProfile()

            profile.website_url = request.POST.get("website_url")
            profile.username = request.POST.get("username")
            profile.password = request.POST.get("password")
            profile.automation_enabled = "automation_enabled" in request.POST
            profile.headless = "headless" in request.POST
            profile.retry_count = int(request.POST.get("retry_count"))
            profile.refresh_interval = int(request.POST.get("refresh_interval"))
            profile.preferred_event = request.POST.get("preferred_event")
            profile.preferred_slot = request.POST.get("preferred_slot")

            profile.save()

            return redirect("/")

        if "start" in request.POST:

            Thread(
                target=start_automation,
                daemon=True,
            ).start()

            return redirect("/")

    return render(
        request,
        "dashboard/dashboard.html",
        {
            "profile": profile,
        },
    )