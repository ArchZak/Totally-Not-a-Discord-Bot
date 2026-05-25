from totally_not_a_bot.server import _client


def get_bot_id_dto():
    """Get the bot's user ID."""
    return _client.user.id
