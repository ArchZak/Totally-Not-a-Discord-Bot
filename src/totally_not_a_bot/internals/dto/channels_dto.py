from server import _client


def fetch_channel_by_id(channel_id: int):
    """
    Fetch a specific channel.

    Args:
        channel_id (int): The ID of the channel to fetch

    Returns:
        channel (): The fetched channel object
    """
    return _client.get_channel(channel_id)
