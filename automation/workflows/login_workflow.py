from automation.pages.login_page import LoginPage
from automation.pages.dashboard_page import DashboardPage

from automation.utils.retry import Retry
from automation.utils.logger import Logger


class LoginWorkflow:

    def __init__(self, page):

        self.login = LoginPage(page)

        self.dashboard = DashboardPage(page)

    def execute(
        self,
        website,
        username,
        password,
    ):

        Logger.info("Starting Login Workflow")

        Retry.execute(

            lambda:

            self.login.login(

                website,

                username,

                password

            )

        )

        self.dashboard.verify_login()

        Logger.success("Login Workflow Completed")