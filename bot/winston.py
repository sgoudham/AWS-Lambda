import logging
import random

from twython import Twython, TwythonError

from bot.aws_secrets import get_secret

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Winston:
    def __init__(self):
        self.bot = Twython(
            app_key=get_secret("CONSUMER_KEY"),
            app_secret=get_secret("CONSUMER_SECRET"),
            oauth_token=get_secret("ACCESS_TOKEN_KEY"),
            oauth_token_secret=get_secret("ACCESS_TOKEN_SECRET"),
        )
        self.potential_tweets = [
            "@PlayOverwatch I didn't pay my taxes!",
            "I'm wanted in over 60 countries!",
            "Overwatch.",
            "Echo!",
            "@PlayOverwatch #LetWinstonWallRide",
            "@PlayOverwatch #LetWinstonWallClimb",
            "Please Delete Echo\n\nSincerely, Winston From Overwatch\n\n@PlayOverwatch",
            "Year of the Winston Event When? @PlayOverwatch",
            "Is This On?",
            "How Embarrassing!",
            "Winston From Overwatch.",
            "Is it too much to ask for some peanut butter covered toes? @PlayOverwatch",
            "I'm holding Sigma hostage in Paris.\nFor every hour Echo isn't nerfed, I will remove one of his toes.\n\n@PlayOverwatch",
            "My new year's resolutions: Less peanut butter, more... bananas.",
            "I'm feeling unstoppable!",
            "I have a crippling addiction to peanut butter."
        ]
        self.potential_tweets_with_images = [
            ["Are You With Me? @PlayOverwatch", "winston_grin.jpg"],
            ["You won't like me when I'm angry.", "winston_angry.jpg"],
            ["Look out world! I'm on a rampage!", "winston_primal_rage.jpg"],
            ["Holy Shit.", "overwatch_meme.jpg"]
        ]

    def send_tweet(self, tweet_text):
        """Sends a tweet to Twitter"""

        self.bot.update_status(status=tweet_text)
        logger.info(f"Tweet Sent: '{tweet_text}'")

    def send_random_tweet(self):
        """Tweet something random from potential tweets"""

        result = random.choice([True, False])
        if result:
            random_tweet = random.choice(self.potential_tweets)
            self.send_tweet(random_tweet)
        else:
            random_tweet_with_image = random.choice(self.potential_tweets_with_images)
            self.tweet_with_media(random_tweet_with_image)

    def tweet_with_media(self, text_and_media):
        """Tweet with media + optional text"""

        text = text_and_media[0]
        filename = text_and_media[1]

        path = f"./media/{filename}"
        media = open(path, 'rb')

        try:
            response = self.bot.upload_media(media=media)
            self.bot.update_status(status=text, media_ids=[response['media_id']])
            logger.info(f"Tweet Sent With Image: || Tweet: {text} || Image Name: {filename}")
        except TwythonError as error:
            print(error.msg)

    def follow_someone(self, username):
        """Follows someone based on given id"""

        self.bot.create_friendship(screen_name=username)
        logger.info(f"Followed User: " f'{username}')

    def like_tweet(self, tweet_id):
        """Likes a tweet based on it's ID"""

        self.bot.create_favorite(id=tweet_id)
        logger.info(f"Liked Tweet, Tweet ID: " f'{tweet_id}')
