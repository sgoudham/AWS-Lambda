def send_tweet(bot, tweet_text):
    """Sends a tweet to Twitter"""

    bot.update_status(status=tweet_text)


def follow_someone(bot, username):
    """Follows someone based on given username"""

    bot.create_friendship(username=username)


def like_tweet(bot, tweet_id):
    """Likes a tweet based on it's ID"""

    bot.create_favorite(id=tweet_id)
