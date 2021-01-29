from twitter.bot.bot import Winston


def send_tweet(tweet_text):
    """Sends a tweet to Twitter"""

    Winston.bot.update_status(status=tweet_text)


def follow_someone(username):
    """Follows someone based on given username"""

    Winston.bot.create_friendship(username=username)


def like_tweet(tweet_id):
    """Likes a tweet based on it's ID"""

    Winston.bot.create_favorite(id=tweet_id)
