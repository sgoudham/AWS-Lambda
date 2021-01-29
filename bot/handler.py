import logging
import random

from bot.commands import send_tweet
from bot.winston import Winston

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def event_handler(event, context):
    """Sends random tweet from list of potential tweets"""
    winston = Winston()

    random_tweet = random.choice(winston.potential_tweets)
    send_tweet(winston.bot, random_tweet)

    logger.info(f"Random Tweet Sent: {random_tweet}")
