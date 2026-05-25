from totally_not_a_bot.server import _client


def fetch_channel_by_id(channel_id: int):
    """Fetch a specific channel."""
    return _client.get_channel(channel_id)
