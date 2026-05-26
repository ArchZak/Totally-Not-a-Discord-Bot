from typing import Annotated, Literal

from totally_not_a_bot.internals.services import profile_services


async def set_bot_status(status: str):
    """
    Set the status of the discord bot.

    Args:
        status (str): The new status for the bot user

    Returns:
        None
    """
    await profile_services.set_bot_status_service(status)


async def set_bot_activity(
    activity_type: Annotated[
        Literal["playing", "streaming", "listening", "watching"],
        'The type of activity (e.g., "playing", "streaming", "listening", "watching")',
    ],
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
    return await profile_services.set_bot_activity_service(activity_type, activity_name)
