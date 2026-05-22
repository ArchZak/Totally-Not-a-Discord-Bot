from server import _client


def get_bot_id_dto():
    """
    Get the bot's user ID.

    Returns:
        int: The bot's user ID
    """
    return _client.user.id
