from twitter.bot.winston import Winston


def handler(event, context):
    """Sends random tweet from list of potential tweets"""
    Winston.request_handler()
