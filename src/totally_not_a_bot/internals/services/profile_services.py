from typing import Literal

import discord
from totally_not_a_bot.config.app import _client

# region Profile Tools


async def set_bot_status_service(status: str):
    """
    Set the status of the discord bot.

    Args:
        status (str): The new status for the bot user

    Returns:
        None
    """
    await _client.change_presence(status=status)


async def set_bot_activity_service(
    activity_type: Literal["playing", "streaming", "listening", "watching"],
    activity_name: str,
):
    """
    Set the activity of the discord bot.

    Args:
        activity_type (str): The type of activity ("playing", "streaming", "listening", "watching")
        activity_name (str): The name of the activity

    Returns:
        None
    """
    activity = discord.Activity(name=activity_name, type=getattr(discord.ActivityType, activity_type, discord.ActivityType.playing))
    await _client.change_presence(activity=activity)


# endregion
