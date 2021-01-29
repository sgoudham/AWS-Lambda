import random
from twython import Twython

from twitter.bot.aws_secrets import get_secret
from twitter.bot.commands import send_tweet


class Winston:
    bot = Twython(
        get_secret("CONSUMER_KEY"),
        get_secret("CONSUMER_SECRET"),
        get_secret("ACCESS_TOKEN_KEY"),
        get_secret("ACCESS_TOKEN_SECRET")
    )

    @staticmethod
    def potential_tweets():
        return [
            "Hello! I'm Winston From Overwatch!",
            "Winston! From! Overwatch!",
            "Winston? From Overwatch?"
        ]

    @staticmethod
    def request_handler():
        send_tweet(random.choice(Winston.potential_tweets()))