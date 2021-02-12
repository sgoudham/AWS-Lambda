import logging
import random

from bot.winston import Winston

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def event_handler(event, context):
    """Sends random tweet from list of potential tweets"""

    winston = Winston()

    Actions = {
        "tweet": lambda text: winston.send_tweet(text),
        "tweet_media": lambda text_and_media: winston.tweet_with_media(text_and_media),
        "like": lambda tweet_id: winston.like_tweet(tweet_id),
        "follow": lambda username: winston.follow_someone(username)
    }

    for key, values in event.items():
        Actions[key](values)

    winston.send_tweet(random.choice(winston.potential_tweets))
