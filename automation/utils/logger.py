from datetime import datetime


class Logger:

    @staticmethod
    def _log(level, message):

        print(

            f"[{level}] "

            f"{datetime.now().strftime('%H:%M:%S')} "

            f"| {message}"

        )

    @classmethod
    def info(cls, msg):

        cls._log("INFO", msg)

    @classmethod
    def success(cls, msg):

        cls._log("SUCCESS", msg)

    @classmethod
    def warning(cls, msg):

        cls._log("WARNING", msg)

    @classmethod
    def error(cls, msg):

        cls._log("ERROR", msg)