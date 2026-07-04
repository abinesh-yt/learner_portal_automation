from automation.pages.base_page import BasePage
from automation.utils.logger import Logger


class LoginPage(BasePage):

    USERNAME = "#id_username"
    PASSWORD = "#id_password"
    LOGIN_BUTTON = "button[type='submit']"

    def login(self, url: str, username: str, password: str):

        Logger.info("Opening Login Page")

        self.open(url)

        Logger.info("Entering Username")

        self.fill(self.USERNAME, username)

        Logger.info("Entering Password")

        self.fill(self.PASSWORD, password)

        Logger.info("Clicking Login")

        self.click(self.LOGIN_BUTTON)