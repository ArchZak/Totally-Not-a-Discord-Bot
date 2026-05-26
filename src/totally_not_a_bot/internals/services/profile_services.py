from typing import Annotated, Literal

import totally_not_a_bot.internals.dto.profiles_dto as profiles_dto

# region Profile Tools


async def set_bot_status_service(status: str):
    """
    Set the status of the discord bot.

    Args:
        status (str): The new status for the bot user

    Returns:
        None
    """
    await profiles_dto.set_bot_status_dto(status)


async def set_bot_activity_service(
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
    await profiles_dto.set_bot_activity_dto(activity_type, activity_name)


# endregion
