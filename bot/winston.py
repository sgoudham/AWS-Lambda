from twython import Twython

from bot.aws_secrets import get_secret


class Winston:
    def __init__(self):
        self.bot = Twython(
            get_secret("CONSUMER_KEY"),
            get_secret("CONSUMER_SECRET"),
            get_secret("ACCESS_TOKEN_KEY"),
            get_secret("ACCESS_TOKEN_SECRET")
        )
        self.potential_tweets = [
            "Hello! I'm Winston From Overwatch!",
            "Winston! From! Overwatch!",
            "Winston? From Overwatch?"
        ]
