from server import _client


async def set_bot_status_dto(status: str):
    """
    Set the status of the discord bot.

    Args:
        status (str): The new status for the bot user

    Returns:
        None
    """
    await _client.change_presence(activity=_client.activity, status=status)


async def set_bot_activity_dto(activity_type: str, activity_name: str):
    """
    Set the activity of the discord bot.

    Args:
        activity_type (str): The type of activity (e.g., "playing", "streaming", "listening", "watching")
        activity_name (str): The name of the activity

    Returns:
        None
    """
    activity = _client.Activity(type=activity_type, name=activity_name)
    await _client.change_presence(activity=activity)
