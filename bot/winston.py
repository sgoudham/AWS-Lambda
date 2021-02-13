import random

import filetype as filetype
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
            "@PlayOverwatch I didn't pay my taxes!",
            "I'm wanted in over 60 countries!",
            "Overwatch",
            "Echo!",
            "@PlayOverwatch #LetWinstonWallRide",
            "@PlayOverwatch #LetWinstonWallClimb",
            "Please Delete Echo\n\nSincerely, Winston From Overwatch\n\n@PlayOverwatch",
            "Year of the Winston Event When? @PlayOverwatch",
            "Are You With Me? @PlayOverwatch",
            "Is This On?",
            "How Embarrassing!",
            "Winston From Overwatch",
            "Is it too much to ask for some peanut butter covered toes? @PlayOverwatch",
            "I'm holding Sigma hostage in Paris.\nFor every hour Echo isn't nerfed, I will remove one of his toes.\n\n@PlayOverwatch",
            "You won't like me when I'm angry."
        ]

    def send_tweet(self, tweet_text):
        """Sends a tweet to Twitter"""

        self.bot.update_status(status=tweet_text)

    def send_random_tweet(self):
        """Tweet something random from potential tweets"""

        self.bot.update_status(status=random.choice(self.potential_tweets))

    def tweet_with_media(self, text_and_media):
        """Tweet with media + optional text"""

        text = text_and_media[0]
        filename = text_and_media[1]

        path = f"./media/{filename}"
        media = open(path, 'rb')

        if filetype.is_image(media):
            response = self.bot.upload_media(media=media.read().decode())
            self.bot.update_status(status=text if text else "Test", media_ids=[response['media_id']])
        elif filetype.is_video(media):
            response = self.bot.upload_video(media=media, media_type='video/mp4')
            self.bot.update_status(media_ids=[response['media_id']])

    def follow_someone(self, username):
        """Follows someone based on given id"""

        self.bot.create_friendship(screen_name=username)

    def like_tweet(self, tweet_id):
        """Likes a tweet based on it's ID"""

        self.bot.create_favorite(id=tweet_id)
